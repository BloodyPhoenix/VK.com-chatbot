from peewee import *

weather_db = SqliteDatabase("weather.db")


class ForecastModel(Model):
    date_full = DateField(formats=["%Y.%m.%d"])
    date_day = CharField()
    date_month = CharField()
    date_weekday = CharField()
    morning_temp = CharField()
    morning_weather = CharField()
    morning_senses = CharField()
    morning_pressure = CharField()
    morning_humidity = CharField()
    morning_wind = CharField()
    day_temp = CharField()
    day_weather = CharField()
    day_senses = CharField()
    day_pressure = CharField()
    day_humidity = CharField()
    day_wind = CharField()
    evening_temp = CharField()
    evening_weather = CharField()
    evening_senses = CharField()
    evening_pressure = CharField()
    evening_humidity = CharField()
    evening_wind = CharField()
    night_temp = CharField()
    night_weather = CharField()
    night_senses = CharField()
    night_pressure = CharField()
    night_humidity = CharField()
    night_wind = CharField()

    class Meta:
        database = weather_db

    @staticmethod
    def _new_row(day: dict):
        ForecastModel.create(
            date_full=day["полная дата"],
            date_day=day["число"],
            date_month=day["месяц"],
            date_weekday=day["день недели"],
            morning_temp=day["утром"]["температура"],
            morning_weather=day["утром"]["погода"],
            morning_senses=day["утром"]["ощущается"],
            morning_pressure=day["утром"]["давление"],
            morning_humidity=day["утром"]["влажность"],
            morning_wind=day["утром"]["ветер"],
            day_temp=day["днём"]["температура"],
            day_weather=day["днём"]["погода"],
            day_senses=day["днём"]["ощущается"],
            day_pressure=day["днём"]["давление"],
            day_humidity=day["днём"]["влажность"],
            day_wind=day["днём"]["ветер"],
            evening_temp=day["вечером"]["температура"],
            evening_weather=day["вечером"]["погода"],
            evening_senses=day["вечером"]["ощущается"],
            evening_pressure=day["вечером"]["давление"],
            evening_humidity=day["вечером"]["влажность"],
            evening_wind=day["вечером"]["ветер"],
            night_temp=day["ночью"]["температура"],
            night_weather=day["ночью"]["погода"],
            night_senses=day["ночью"]["ощущается"],
            night_pressure=day["ночью"]["давление"],
            night_humidity=day["ночью"]["влажность"],
            night_wind=day["ночью"]["ветер"]
        )

    @staticmethod
    def _update_row(day: dict):
        day_data = ForecastModel.get(ForecastModel.date_full == day["полная дата"])
        day_data.morning_temp = day["утром"]["температура"],
        day_data.morning_weather = day["утром"]["погода"],
        day_data.morning_senses = day["утром"]["ощущается"],
        day_data.morning_pressure = day["утром"]["давление"],
        day_data.morning_humidity = day["утром"]["влажность"],
        day_data.morning_wind = day["утром"]["ветер"],
        day_data.day_temp = day["днём"]["температура"],
        day_data.day_weather = day["днём"]["погода"],
        day_data.day_senses = day["днём"]["ощущается"],
        day_data.day_pressure = day["днём"]["давление"],
        day_data.day_humidity = day["днём"]["влажность"],
        day_data.day_wind = day["днём"]["ветер"],
        day_data.evening_temp = day["вечером"]["температура"],
        day_data.evening_weather = day["вечером"]["погода"],
        day_data.evening_senses = day["вечером"]["ощущается"],
        day_data.evening_pressure = day["вечером"]["давление"],
        day_data.evening_humidity = day["вечером"]["влажность"],
        day_data.evening_wind = day["вечером"]["ветер"],
        day_data.night_temp = day["ночью"]["температура"],
        day_data.night_weather = day["ночью"]["погода"],
        day_data.night_senses = day["ночью"]["ощущается"],
        day_data.night_pressure = day["ночью"]["давление"],
        day_data.night_humidity = day["ночью"]["влажность"],
        day_data.night_wind = day["ночью"]["ветер"]
        day_data.save

    @staticmethod
    def update_table(day):
        days = ForecastModel.select()
        days_dates = []
        for date in days:
            days_dates.append(date.date_full)
        if str(day["полная дата"]) in days_dates:
            ForecastModel._update_row(day)
        else:
            ForecastModel._new_row(day)
