# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import os.path
import zipfile


class EventsCounter:

    def __init__(self, file_name, path=None):
        self.file_name = file_name
        self.event_log = []
        self.nok_events = {}
        if path:
            self.path = os.path.normpath(path)
        else:
            self.path = os.getcwd()

    def check_file_format(self):
        if self.file_name.endswith(".txt"):
            return True
        else:
            print("Работа с файлами, отличными от формата txt, не поддерживается")
            return False

    def find_file_directory(self):
        if self.check_file_format():
            dirs = os.walk(self.path)
            for dir_path, _, files in dirs:
                for file in files:
                    if self.check_file_name(file):
                        normpath = os.path.normpath(dir_path)
                        os.chdir(normpath)
                        return True
        print("Запрашиваемый файл не найден в данной директории или вложенных.")
        return False

    def check_file_name(self, file):
        if self.file_name == file:
            return True
        elif zipfile.is_zipfile(file):
            archive = zipfile.ZipFile(file, "r")
            content = archive.namelist()
            if self.file_name in content:
                archive.extract(self.file_name)
                return True

    def prepare_logs(self):
        with open(self.file_name, "r", encoding="cp1251") as file:
            for line in file:
                prepare_log = line.split()
                log_date = prepare_log[0].strip("[")
                log_time = prepare_log[1].strip("]")
                log_status = prepare_log[2]
                log = (log_date, log_time, log_status)
                self.event_log.append(log)

    def count_noks(self):
        if self.find_file_directory():
            self.prepare_logs()
            for event in self.event_log:
                if event[-1] == "NOK":
                    nok_event_date = event[0]
                    nok_event_time = event[1][:5]
                    nok_event = str("[" + nok_event_date + " " + nok_event_time + "]")
                    if nok_event in self.nok_events:
                        self.nok_events[nok_event] = self.nok_events[nok_event] + 1
                    else:
                        self.nok_events[nok_event] = 1
            self.save_results()

    def save_results(self):
        with open("NOK count.txt", "a+", encoding="cp1251") as file:
            for key in self.nok_events:
                value = str(self.nok_events[key])
                file.write(key + " " + value)


test = EventsCounter("events.txt")
test.count_noks()

# TODO вывод лучше делаем в колонку


# После зачета первого этапа нужно сделать группировку событий
# TODO вот такие группировки
#  - по часам - [2018-05-14 19]
#  - по месяцу - [2018-05]
#  - по году - [2018]
