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

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    @staticmethod
    def switch_directory(file_name):
        path = os.getcwd()
        dirs = os.walk(path)
        for directory in dirs:
            normpath = os.path.normpath(directory[0])
            os.chdir(normpath)
            if file_name in directory[2]:
                break
            else:
                for file in directory[2]:
                    if zipfile.is_zipfile(file):
                        archive = zipfile.ZipFile(file, "r")
                        content = archive.namelist()
                        if file_name in content:
                            archive.extract(file_name)
                            break

    @staticmethod
    def prepare_file(file_name):
        event_log = []
        with open(file_name, "r", encoding="cp1251") as file:
            for line in file:
                prepare_log = line.split()
                log_date = prepare_log[0].strip("[")
                log_time = prepare_log[1].strip("]")
                log_status = prepare_log[2]
                log = (log_date, log_time, log_status)
                event_log.append(log)
        return event_log

    @staticmethod
    def count_noks(file_name):
        EventsCounter.switch_directory(file_name=file_name)
        event_log = EventsCounter.prepare_file(file_name)
        nok_events = {}
        for event in event_log:
            if event[-1] == "NOK":
                nok_event_date = event[0]
                nok_event_time = event[1][:5]
                nok_event = str("["+nok_event_date+" "+nok_event_time+"]")
                if nok_event in nok_events:
                    nok_events[nok_event] = nok_events[nok_event]+1
                else:
                    nok_events[nok_event] = 1
        EventsCounter.save_results(nok_events)

    @staticmethod
    def save_results(result):
        with open("NOK count.txt", "a+", encoding="cp1251") as file:
            for key in result:
                value = str(result[key])
                file.write(key+" "+value)


EventsCounter.count_noks("events.txt")


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
