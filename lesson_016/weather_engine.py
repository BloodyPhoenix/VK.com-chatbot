from urllib.request import urlopen

import peewee
from bs4 import BeautifulSoup
from db_init import *
import re
import datetime
import argparse
import image_maker

_MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 20, 12: 31}


class DayForecast:
    """makes a dictionary, containing one day forecast in self.forecast param"""

    def __init__(self, data: list):
        self.data = data  # incoming data
        self.date = datetime.date.today()
        self.weekday = datetime.date.weekday(self.date)
        self.day_parts = ["утром", "днём", "вечером", "ночью"]
        if "завтра" in self.data:
            if self.weekday < 6:
                self.weekday += 1
            else:
                self.weekday = 0
        self.forecast = {}  # output

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
            self.forecast[day_part]["температура"] = self.forecast[day_part]["температура"].replace("…", " ")


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
        self.first_day_request = None
        self.second_day_request = None
        weather_db.connect()
        weather_db.create_tables([ForecastModel])
        ForecastModel.create_table()

    def run(self):
        command_help = """Введите команду:
1. обновить - обновляет базу прогнозов
2. карточка - создаёт карточку с прогнозом
3. прогноз - вывести прогноз за определённые даты на консоль
4. архив - показать все числа, за которые есть прогноз в базе"""
        self.second_day_request = datetime.date.today()
        try:
            today = ForecastModel.select().where(ForecastModel.date_full == self.second_day_request).get()
            self.second_day_request = today.id
            if today.id > 6:
                self.first_day_request = self.second_day_request - 6
            else:
                self.first_day_request = 1
            self._return_data()
        except peewee.DoesNotExist:
            print("Нет данных для отображения. Перед началом работы обновите базу.")
        while True:
            print("""Введите команду. Введите "помощь", чтобы увидеть перечень команд""")
            command = input()
            print()
            if "обновить" == command:
                self._update()
                print("База успешно обновлена!")
            elif "помощь" == command:
                print(command_help)
            elif "карточка" == command:
                self._card_options()
            elif "прогноз" == command:
                self._forecast_options()
            elif "архив" == command:
                results = ForecastModel.select()
                for result in results:
                    print(result.date_full)
            else:
                print("Неизвестная команда")
            print()

    def _forecast_options(self):
        while True:
            print("""Введите первую дату в формате дд-мм-гггг""")
            self.first_day_request = input()
            try:
                self.first_day_request = self._input_convert(self.first_day_request)
            except Exception as exc:
                self._print_error(exc)
                continue
            while True:
                print("""Введите вторую дату в формате дд-мм-гггг""")
                self.second_day_request = input()
                try:
                    self.second_day_request = self._input_convert(self.second_day_request)
                except Exception as exc:
                    self._print_error(exc)
                    continue
                break
            try:
                first_id = ForecastModel.select().where(ForecastModel.date_full == self.first_day_request).get()
            except peewee.DoesNotExist:
                print("Такого числа нет в базе. Обновите базу.")
                continue
            self.first_day_request = first_id.id
            try:
                second_id = ForecastModel.select().where(ForecastModel.date_full == self.second_day_request).get()
            except peewee.DoesNotExist:
                print("Такого числа нет в базе. Обновите базу.")
                continue
            self.second_day_request = second_id.id
            self._return_data()
            return

    @staticmethod
    def _input_convert(day):
        day = day.split("-")
        day = day[::-1]
        for index in range(len(day)):
            day[index] = int(day[index])
        return datetime.date(*day)

    @staticmethod
    def _print_error(error):
        print()
        print("Извините, произошла ошибка. Проверьте корректность воодимых данных и повторите ввод")
        print(f"{error}. {error.args}")

    def _card_options(self):
        while True:
            print("""Введите данные в формате дд-мм-гггг или введите"сегодня".""")
            self.first_day_request = input()
            if "с" in self.first_day_request:
                self.first_day_request = None
                self._make_card()
            elif "назад" in self.first_day_request:
                self.first_day_request = None
                return
            else:
                try:
                    self.first_day_request = self._input_convert(self.first_day_request.split)
                    self._make_card()
                except Exception as exc:
                    self._print_error(exc)
                    continue
            self.first_day_request = None
            return

    def _get_full_data(self):
        year = datetime.date.today().year
        december = False
        january = False
        self.new_forecast = DayCardReader(self.url).start()
        month_number = {"янв": "01", "фев": "02", "мар": "03", "апр": "04", "май": "05", "июн": "06",
                        "июл": "07", "авг": "08", "сен": "09", "окт": "10", "ноя": "11", "дек": "12"}
        for day in self.new_forecast:
            for month in month_number:
                # Проверяем, не меняется ли в прогнозе год, так как Яндекс год не показывает
                if month in day["месяц"]:
                    if "дек" == month:
                        december = True
                    if "янв" == month:
                        january = True
                    if december and january:
                        year += 1
                        december = False
                    day["полная дата"] = datetime.date(int(year), int(month_number[month]), int(day["число"]))

    def _update(self):
        self._get_full_data()
        for day in self.new_forecast:
            ForecastModel.update_table(day)

    def _return_data(self):
        if self.second_day_request > self.first_day_request:
            results = ForecastModel.select().where((ForecastModel.id > self.first_day_request - 1) &
                                                   (ForecastModel.id < self.second_day_request + 1))
        else:
            results = ForecastModel.select().where(ForecastModel.id == 1)
        for result in results:
            print(result.date_day, result.date_month)
            print(result.date_weekday)
            print()
            print("Утром:")
            print(result.morning_temp)
            print("Ощущается:", result.morning_senses)
            print(result.morning_weather)
            print("Давление", result.morning_pressure)
            print("Влажность", result.morning_humidity)
            print("Ветер:", result.morning_wind)
            print()
            print("Днём:")
            print(result.day_temp)
            print("Ощущается:", result.day_senses)
            print(result.day_weather)
            print("Давление", result.day_pressure)
            print("Влажность", result.day_humidity)
            print("Ветер:", result.day_wind)
            print()
            print("Вечером:")
            print(result.evening_temp)
            print("Ощущается:", result.evening_senses)
            print(result.evening_weather)
            print("Давление", result.evening_pressure)
            print("Влажность", result.evening_humidity)
            print("Ветер:", result.evening_wind)
            print()
            print("Ночью:")
            print(result.night_temp)
            print("Ощущается:", result.night_senses)
            print(result.night_weather)
            print("Давление", result.night_pressure)
            print("Влажность", result.night_humidity)
            print("Ветер:", result.night_wind)
            print()
            print()
        self.first_day_request = None
        self.second_day_request = None

    def _make_card(self):
        if self.first_day_request:
            try:
                today_forecast = ForecastModel.select().where(ForecastModel.date_full == self.first_day_request).get()
            except peewee.DoesNotExist:
                print("Такого числа нет в базе. Обновите базу.")
                return
            current_weather = today_forecast.day_weather
        else:
            current_hour = datetime.datetime.now().hour
            current_day = datetime.datetime.today()
            if current_day.month < 10:
                month = "0" + str(current_day.month)
            else:
                month = str(current_day.month)
            if current_day.day < 10:
                day = "0" + str(current_day.day)
            else:
                day = str(current_day.day)
            current_day = str(current_day.year) + "-" + month + "-" + day
            try:
                today_forecast = ForecastModel.select().where(ForecastModel.date_full == current_day).get()
            except peewee.DoesNotExist:
                print("В базе ничего нет! Обновите базу.")
                return
            if current_hour < 6:
                current_weather = today_forecast.night_weather
            elif current_hour < 12:
                current_weather = today_forecast.morning_weather
            elif current_hour < 18:
                current_weather = today_forecast.day_weather
            else:
                current_weather = today_forecast.evening_weather
        if "дождь" in current_weather.lower():
            weather = "rainy"
        elif "ливень" in current_weather.lower():
            weather = "rainy"
        elif "облач" in current_weather.lower():
            weather = "cloudy"
        elif "пасмур" in current_weather.lower():
            weather = "cloudy"
        elif "снег" in current_weather.lower():
            weather = "snow"
        elif "метель" in current_weather.lower():
            weather = "snow"
        else:
            weather = "clear"
        weather_data = [today_forecast.date_weekday,
                        today_forecast.date_day,
                        today_forecast.date_month,
                        today_forecast.morning_temp,
                        today_forecast.morning_senses,
                        today_forecast.morning_pressure,
                        today_forecast.morning_humidity,
                        today_forecast.morning_wind,
                        today_forecast.day_temp,
                        today_forecast.day_senses,
                        today_forecast.day_pressure,
                        today_forecast.day_humidity,
                        today_forecast.day_wind,
                        today_forecast.evening_temp,
                        today_forecast.evening_senses,
                        today_forecast.evening_pressure,
                        today_forecast.evening_humidity,
                        today_forecast.evening_wind,
                        today_forecast.night_temp,
                        today_forecast.night_senses,
                        today_forecast.night_pressure,
                        today_forecast.night_humidity,
                        today_forecast.night_wind,
                        today_forecast.morning_weather,
                        today_forecast.day_weather,
                        today_forecast.evening_weather,
                        today_forecast.night_weather
                        ]
        card = image_maker.ImageMaker(weather, weather_data)
        card.make_card()


if __name__ == "__main__":
    forecast_maker = WeatherMaker()
    forecast_maker.run()
