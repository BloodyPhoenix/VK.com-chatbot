# -*- coding: utf-8 -*-

import os.path
import time
import shutil
import zipfile

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
        self.current_path = None
        self.target_path = None
        self.current_file = None
        self.file_time = None
        self.file_name = None
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
                self.file_name = os.path.basename(file)
                self.current_path = os.path.join(dir_path, file)
                self.move_file()

    def move_file(self):
        self.get_target_path()
        os.chdir(self.root_dir)
        os.chdir(self.target_dir)
        full_path = os.path.join(self.target_path, self.file_name)
        if not os.path.exists(full_path):
            if not os.path.exists(self.file_year):
                os.mkdir(self.file_year)
            os.chdir(self.file_year)
            if not os.path.exists(self.file_month):
                os.mkdir(self.file_month)
            os.chdir(self.root_dir)
            self.copy_file()

    def copy_file(self):
        shutil.copy2(self.current_path, self.target_path)

    def get_time(self):
        self.file_time = os.path.getmtime(self.current_path)
        self.file_time = time.gmtime(self.file_time)

    def get_target_path(self):
        self.get_time()
        self.file_year = str(self.file_time[0])
        self.file_month = str(self.file_time[1])
        self.target_path = os.path.join(self.target_dir, self.file_year, self.file_month)


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html


class SortZipFiles(SortFiles):

    def change_dir(self):
        dirs = os.walk(self.start_path)
        for dir_path, _, files in dirs:
            if self.start_dir in files:
                self.root_dir = dir_path
                os.chdir(self.root_dir)
                if not os.path.exists(self.target_dir):
                    os.mkdir(self.target_dir)
                return True
        print("В указанной директории запрашиваемый архив не найден.")
        return False

    def move_all_files(self):
        self.change_dir()
        path = os.path.join(self.root_dir, str(self.start_dir))
        with zipfile.ZipFile(path, "r") as self.start_dir:
            content = self.start_dir.namelist()
            for item in content:
                self.current_path = self.start_dir.getinfo(item)
                if not self.current_path.is_dir():
                    self.file_name = os.path.basename(self.current_path.filename)
                    self.current_file = item
                    self.move_file()

    def get_time(self):
        self.file_time = self.current_path.date_time

    def copy_file(self):
        source = self.start_dir.read(self.current_file)
        target = os.path.join(self.target_path, self.file_name)
        with open(target, "wb") as target_file:
            target_file.write(source)
        file_time = self.file_time + (0, 0, 0)
        file_time = time.mktime(file_time)
        os.utime(target, (file_time, file_time))


test = SortZipFiles("icons.zip", "icons_by_year")
test.move_all_files()

# зачет!
