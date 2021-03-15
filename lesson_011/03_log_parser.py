# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

import os
import zipfile
from collections import defaultdict


class MinutesEventCounter:

    def __init__(self, file_name, path=None):
        self.file_name = file_name
        self.event_log = []
        self.nok_events = defaultdict(int)
        if path:
            self.path = os.path.normpath(path)
        else:
            self.path = os.getcwd()
        self.check_file_format()
        self.find_file_directory()
        with open(self.file_name, "r", encoding="cp1251") as file:
            self.prepare_logs(file)
        self.nok_events = list(self.nok_events.items())
        self.nok_events.sort(key=lambda x: x)
        self.iteration_counter = 0

    def check_file_format(self):
        if not self.file_name.endswith(".txt"):
            raise TypeError("Работа с файлами, отличными от формата txt, не поддерживается")

    def find_file_directory(self):
        dirs = os.walk(self.path)
        for dir_path, _, files in dirs:
            for file in files:
                if self.check_file_name(file):
                    normpath = os.path.normpath(dir_path)
                    os.chdir(normpath)
                    return True
        raise OSError("Запрашиваемый файл не найден в данной директории или вложенных.")

    def check_file_name(self, file):
        if self.file_name == file:
            return True
        elif zipfile.is_zipfile(file):
            archive = zipfile.ZipFile(file, "r")
            content = archive.namelist()
            if self.file_name in content:
                archive.extract(self.file_name)
                return True

    def __iter__(self):
        self.iteration_counter = -1
        return self

    def __next__(self):
        self.iteration_counter += 1
        if self.iteration_counter == len(self.nok_events):
            raise StopIteration()
        return self.nok_events[self.iteration_counter]

    def prepare_logs(self, file):
        for line in file:
            prepare_log = line.split()
            log_date = prepare_log[0].strip("[")
            log_time = prepare_log[1].strip("]")
            log_time = log_time[:5]
            log_status = prepare_log[2]
            log = (log_date, log_time, log_status)
            self.save_log(log)

    def save_log(self, log):
        if log[-1] == "NOK":
            log_datetime = log[0] + " " + log[1]
            self.nok_events[log_datetime] += 1

#
# count_noks = MinutesEventCounter("events.txt")
# for time, value in count_noks:
#     print(time, value)


def count_noks_generator(file_name):
    nok_date_time = ""
    nok_counter = 0
    with open(file_name, "r", encoding="cp1251") as event_log:
        for line in event_log:
            prepare_log = line.split()
            log_status = prepare_log[2]
            if log_status == "NOK":
                log_date = prepare_log[0].strip("[")
                log_time = prepare_log[1].strip("]")
                log_time = log_time[:5]
                log_date_time = log_date + " " + log_time
                if len(nok_date_time) > 0:
                    if log_date_time != nok_date_time:
                        yield nok_date_time, nok_counter
                        nok_date_time = ""
                        nok_counter = 0
                    else:
                        nok_counter += 1
                else:
                    nok_date_time = log_date_time
                    nok_counter += 1


noks_generator = count_noks_generator("events.txt")
for nok_counter in noks_generator:
    print(*nok_counter)


# зачет!
