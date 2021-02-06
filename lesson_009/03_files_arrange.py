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

    def __init__(self, start_dir, target_dir, path=None):
        self.start_dir = start_dir
        self.target_dir = target_dir
        self.root_dir = None
        self.files_time = []
        self.folder_names = {}
        self.current_file = None
        self.current_path = None
        self.target_path = None
        self.file_year = ""
        self.file_month = ""

        if path:
            self.start_path = os.path.normpath(path)
        else:
            self.start_path = os.getcwd()

    def change_dir(self):
        dirs = os.walk(self.start_path)
        for dir_path, *_, in dirs:
            # Мне кажется, тут нужна получше защита от возмножных совпадений имён папок, но я не могу придумать
            if dir_path.endswith(self.start_dir):
                # Тут мы переходим от корня конкретно в директорию, с которой будем работать, и сохраняем точный путь
                # до неё, он потребуется потом
                self.start_path = dir_path
                os.chdir(self.start_path)
                return True
        print("В указанной директории запрашиваемая поддиректория не найдена.")
        return False

    def create_target_dir(self):
        if self.change_dir():
            os.chdir("..")
            self.root_dir = os.getcwd()
            if not os.path.exists(self.target_dir):
                os.mkdir(self.target_dir)

    def move_all_files(self):
        self.create_target_dir()
        os.chdir(self.start_path)
        dirs = os.walk(self.start_path)
        for dir_path, _, files in dirs:
            for file in files:
                self.current_file = file
                self.current_path = os.path.join(dir_path, file)
                self.move_file()

    def move_file(self):
        self.get_target_path()
        os.chdir(self.root_dir)
        os.chdir(self.target_dir)
        if not os.path.exists(self.file_year):
            os.mkdir(self.file_year)
        os.chdir(self.file_year)
        if not os.path.exists(self.file_month):
            os.mkdir(self.file_month)
        os.chdir(self.root_dir)
        shutil.copy2(self.current_path, self.target_path)

    def get_target_path(self):
        file_time = os.path.getmtime(self.current_path)
        file_time = time.gmtime(file_time)
        self.file_year = str(file_time[0])
        self.file_month = str(file_time[1])
        self.target_path = os.path.join(self.target_dir, self.file_year, self.file_month)


test = SortFiles("icons", "icons_by_year")
test.move_all_files()


# TODO хорошо делаем вторую часть, незабываем что нужно сделать так что бы дата изменения была та которая
# TODO хранится в мета данных в зип архиве

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
