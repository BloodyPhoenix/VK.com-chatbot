from urllib.request import urlopen
from bs4 import BeautifulSoup
from db_init import *
import re
import datetime
import argparse

yandex_weather = urlopen("https://yandex.ru/pogoda/moscow")
yandex_soup = BeautifulSoup(yandex_weather.read(), features="html.parser")
yandex_temp_by_day = yandex_soup.find_all("span", {"class": "temp__value temp__value_with-unit"})
yandex_pressure = yandex_soup.find("div", {"aria-label": re.compile("Давление")})
yandex_weather = yandex_soup.find_all("span", {"aria-label": re.compile("В")})

print(yandex_pressure.text)


class DayForecast:
    """makes a dictionary, containing one day forecast in self.forecast param"""
    def __init__(self, data: list):
        self.data = data #incoming data
        self.date = datetime.date.today()
        self.weekday = datetime.date.weekday(self.date)
        self.day_parts = ["утром", "днём", "вечером", "ночью"]
        if "завтра" in self.data:
            if self.weekday < 6:
                self.weekday += 1
            else:
                self.weekday = 0
        self.forecast = {} #output

    def make_forecast(self):
        """Main func"""
        self.forecast["число"] = self.data[0]
        self.forecast["месяц"] = self.data[1]
        if "сегодня" in self.data[2]:
            self.forecast["день недели"] = self._convert_weekday()
        elif "завтра" in self.data[2]:
            self.forecast["день недели"] = self._convert_weekday()
        else:
            self.forecast["день недели"] = self.data[2]
        self._day_forecast()
        self._temp_format()
        return self.forecast

    def _convert_weekday(self):
        """Converts "сегодня" and "завтра" to weekdays"""
        if 0 == self.weekday:
            return "понедельник"
        if 1 == self.weekday:
            return "вторник"
        if 2 == self.weekday:
            return "среда"
        if 3 == self.weekday:
            return "четверг"
        if 4 == self.weekday:
            return "пятница"
        if 5 == self.weekday:
            return "суббота"
        else:
            return "воскресенье"

    def _day_forecast(self):
        """Makes forecast by day parts from incoming data"""
        base_index = 3
        forecast_params = ["температура", "погода", "давление", "влажность", "ветер", "ощущается"]
        for part in self.day_parts:
            daytime = {}
            for param in forecast_params:
                daytime[param] = self.data[base_index]
                base_index += 1
            self.forecast[part] = daytime

    def _temp_format(self):
        """Reformat day part temperature"""
        for day_part in self.day_parts:
            self.forecast[day_part]["температура"] = self.forecast[day_part]["температура"][len(day_part):]


class DayCardReader:
    """Gets data from yandex.weather and makes a list of forecasts"""
    def __init__(self, url):
        self.weather_url = urlopen(url)
        self.weather_soup = BeautifulSoup(self.weather_url.read(), features="html.parser")
        self.headers = self.weather_soup.find_all("dt", {"class": re.compile("forecast-details__day")})
        self.weather = self.weather_soup.find_all("tbody", {"class": "weather-table__body"})
        self.used_tags = set()
        self.days = []
        self.day_data = []

    def start(self):
        for index, header in enumerate(self.headers):
            self.day_data = []
            self.used_tags.clear()
            self._get_header_text(header)
            for row in self.weather[index]:
                self._get_forecast_text(row)
            if self.day_data:
                day_forecast = DayForecast(self.day_data).make_forecast()
                self.days.append(day_forecast)
        return self.days

    def _get_header_text(self, obj):
        children = obj.findChildren()
        if len(children) < 1:
            if obj not in self.used_tags:
                self.used_tags.add(obj)
                if len(obj.text) > 0:
                    self.day_data.append(obj.text)
        else:
            for child in children:
                self._get_header_text(child)

    def _get_forecast_text(self, obj):
        for tag in obj:
            if len(tag.text) > 0:
                self.day_data.append(tag.text)


class WeatherMaker:
    def __init__(self):
        self.url = "https://yandex.ru/pogoda/moscow/details?via=ms#31"
        self.today_forecast = None
        self.forecast = None
        self.options = []
        self.new_forecast = None
        weather_db.connect()
        weather_db.create_tables([ForecastModel])

    def run(self):
        parser = argparse.ArgumentParser()
        while True:
            args = parser.parse_args()
            for argument in args.attrs:
                if argument in self.options:
                    pass

    def _get_full_data(self):
        year = datetime.date.today().year
        december = False
        january = False
        self.new_forecast = DayCardReader(self.url).start()
        month_number = {"янв": "01", "фев": "02", "мар": "03", "апр": "04", "май": "05", "июн": "06",
                        "июл": "07", "авг": "08", "сен": "09", "окт": "10", "ноя": "11", "дек": "12"}
        for day in self.new_forecast:
            for month in month_number:
                if month in day["месяц"]:
                    if "дек" == month:
                        december = True
                    if "янв" == month:
                        january = True
                    if december and january:
                        year += 1
                        december = False
                    day["полная дата"] = day["число"] + "." + month_number[month] + "." + str(year)

    def _update(self):
        self._get_full_data()
        for day in self.new_forecast:
            ForecastModel.update_table(day)


weather = WeatherMaker()
ForecastModel.create_table()
weather._update()
for day in (ForecastModel.select()):
    print(day)

