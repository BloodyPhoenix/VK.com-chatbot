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

    def __init__(self, start_dir, target_dir, path):
        self.start_dir = start_dir
        self.target_dir = target_dir
        self.files_time = []
        self.folder_names = {}
        self.start_path = None
        if path:
            self.path = os.path.normpath(path)
        else:
            self.path = os.getcwd()

    def change_dir(self):
        dirs = os.walk(self.path)
        for directory in dirs:
            normpath = os.path.normpath(directory[0])
            # Мне кажется, тут нужна получше защита от возмножных совпадений имён папок, но я не могу придумать
            if directory[0].endswith(self.start_dir):
                # Тут мы переходим от корня конкретно в директорию, с которой будем работать, и сохраняем точный путь
                # до неё, он потребуется потом
                self.start_path = normpath
                return True
        print("В указанной директории запрашиваемая поддиректория не найдена.")
        return False

    def get_date(self):
        if self.change_dir():
            dirs = os.walk(self.start_path)
            for _, _, files in dirs:
                self.get_files_date(files)
        self.files_time.sort()

    def get_files_date(self, files):
        for file_name in files:
            file_path = os.path.abspath(file_name)
            file_time = os.path.getmtime(file_path)
            file_time = time.gmtime(file_time)
            self.files_time.append(file_time)

    def set_folder_names(self):
        self.get_date()
        for date in self.files_time:
            year = str(date[0])
            month = str(date[1])
            if year not in self.folder_names:
                self.folder_names[year] = []
            if month not in self.folder_names[year]:
                self.folder_names[year].append(month)

    def make_folders(self):
        # Т.к. на предыдущем этапе, перебирая файлы, мы могли уйти неизвестно куда в глубинах исходной папки
        # тут возвращаемся в неё, а потом на уровень выше, чтобы там создать целевую папку
        os.chdir(self.start_path)
        os.chdir('..')
        if not os.path.exists(self.target_dir):
            os.mkdir(self.target_dir)
        os.chdir(self.target_dir)
        for year in self.folder_names:
            # Тут уже идёт большая вложенность, но не знаю, следует ли что-то с этим делать, так как по логике это
            # всё операция создания папок
            if not os.path.exists(year):
                os.mkdir(year)
                os.chdir(year)
                for month in self.folder_names[year]:
                    if not os.path.exists(month):
                        os.mkdir(month)
                os.chdir('..')

    def move_files(self, files, path):
        for file_name in files:
            file_path = os.path.abspath(file_name)
            file_time = os.path.getmtime(file_path)
            file_time = time.gmtime(file_time)
            file_year = str(file_time[0])
            file_month = str(file_time[1])
            target_pass = os.path.join(self.target_dir, file_year, file_month)
            # Переключения директорий тут очень важны!
            # Если не выйдем в общую - ничего не сработает
            os.chdir(self.start_path)
            os.chdir('..')
            shutil.copy2(file_path, target_pass)
            # А тут надо обязательно вернуться в изначальную директорию, где у нас лежат файлы, которые перебираем
            os.chdir(path)

    def sort_files(self):
        self.change_dir()
        self.set_folder_names()
        self.make_folders()
        os.chdir(self.start_path)
        dirs = os.walk(self.start_path)
        for dir_path, _, files in dirs:
            normpath = os.path.normpath(dir_path)
            # Вот тут переключение обязательно, так как мы работаем с этими файлами, а не просто их просматриваем
            os.chdir(normpath)
            self.move_files(files, path=normpath)


# TODO нехватает параметра
sort = SortFiles("icons", "icons_by_year")
sort.sort_files()

# TODO циклом проходимся по списку имен файлов

# TODO напишу тут алгоритм!
# TODO получаем полный путь к файлу используя os.path.join
# TODO получаем данные о времени файла, используя getmtime gmtime, можно разными строками
# TODO получаем месяц и год из ранее полученного объекта данных
# TODO получаем получаем конечный путь кода куда будем писать файл
# TODO тут мы используем join(directory_path папку_куда_пишем год месяц) - 4 аргумента
# TODO далее проверяем есть ли данная папка если нет то создаем
# TODO и в конце используем shutil.copy2 с нужными параметрами (куда копируем и что копируем)

# TODO ориентировочно 9-10 строк

# TODO да можно добавить дополнительный метод на проверку, или создание директории

# TODO код выше нужно сокращать, очень много циклов повторяющихся

# TODO for dirpath, _, filenames in os.walk(self.start_path) - должет быть один

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
