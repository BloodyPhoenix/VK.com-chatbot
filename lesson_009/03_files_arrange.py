# -*- coding: utf-8 -*-

import os.path
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class SortFiles:

    def __enter__(self):
        return self

    def __exit__(self):
        return

    def __init__(self):
        self.base_path = None
        self.files_time = []
        self.folder_names = {}

    def change_dir(self, dir_name):
        path = os.getcwd()
        dirs = os.walk(path)
        for directory in dirs:
            normpath = os.path.normpath(directory[0])
            os.chdir(normpath)
            if directory[0].endswith(dir_name):
                self.base_path = normpath
                break

    def get_date(self, dir_name):
        self.change_dir(dir_name)
        dirs = os.walk(self.base_path)
        for directory in dirs:
            normpath = os.path.normpath(directory[0])
            os.chdir(normpath)
            for file_name in directory[2]:
                file_path = os.path.abspath(file_name)
                file_time = os.path.getmtime(file_path)
                file_time = time.gmtime(file_time)
                self.files_time.append(file_time)
        self.files_time.sort()

    def set_folder_names(self, dir_name):
        self.get_date(dir_name)
        for date in self.files_time:
            year = str(date[0])
            month = str(date[1])
            if year not in self.folder_names:
                self.folder_names[year] = []
            if month not in self.folder_names[year]:
                self.folder_names[year].append(month)

    def make_folders(self, target_dir):
        os.chdir(self.base_path)
        os.chdir('..')
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        os.chdir(target_dir)
        for year in self.folder_names:
            if not os.path.exists(year):
                os.mkdir(year)
                os.chdir(year)
                for month in self.folder_names[year]:
                    if not os.path.exists(month):
                        os.mkdir(month)
                os.chdir('..')

    def sort_files(self, start_dir, target_dir):
        self.change_dir(start_dir)
        self.set_folder_names(start_dir)
        self.make_folders(target_dir)
        os.chdir(self.base_path)
        dirs = os.walk(self.base_path)
        for directory in dirs:
            normpath = os.path.normpath(directory[0])
            os.chdir(normpath)
            for file_name in directory[2]:
                file_path = os.path.abspath(file_name)
                file_time = os.path.getmtime(file_path)
                file_time = time.gmtime(file_time)
                file_year = str(file_time[0])
                file_month = str(file_time[1])
                target_pass = os.path.join(target_dir, file_year, file_month)
                os.chdir(self.base_path)
                os.chdir('..')
                shutil.copy2(file_path, target_pass)
                os.chdir(normpath)


os.chdir('..')
sort = SortFiles()
sort.sort_files("icons", "icons_by_year")




# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
