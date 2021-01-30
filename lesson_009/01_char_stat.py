# -*- coding: utf-8 -*-

import os.path
import zipfile

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


# TODO далее с этого модуля будем практиковать ООП думаю вы его точно поймете

# TODO Я понимаю концепцию и её пользу, но я не понимаю, зачем пихать её туда, где можно обойтись другим стилем
# TODO Если бы мне так нравилась эта концепция, я бы пошла учить C# или Java
# TODO Тут задача, которая элементарно решается без применения классов.


class InOutBlock:

    def __init__(self, file_name):
        self.file_name = file_name
        self.statistics = {}
        self.letters_total = 0



    # TODO мы знаем что файл лежит в python_snippets так давай его от туда возьмем без этих танцев с бубнами
    # TODO сразу при инициализации зададим нужный путь до него

    # TODO А потом нам понадобится применить этот скрипт к файлу, который лежит в другой папке
    # TODO и совершенно ВНЕЗАПНО ничего не сработает.
    # TODO Сейчас скрипт хотя бы обрабатывает хотя бы все вложенные папки от директории запуска
    # TODO А если мы привязываемся к "безусловной" папке python_snippets, то можно сделать проще.
    # TODO os.chdir("python_snippets")
    # TODO Нам же не нужно даже подобие универсальности скрипта...

    # TODO тут пишем метод который распаковывает архив
    # TODO и переопределяет self.file_name

    # TODO Что-то у меня опять сомнения, что это повысит способность скрипта обрабатывать файлы помимо заданных условием
    # TODO Наверное, потому, что оно отработает только с конкретным архивом с конкретным содержимым.

    def find_file_directory(self):
        # получаем текущую рабочую директорию
        path = os.getcwd()
        # получаем список директорий и поддиректорий в ней
        dirs = os.walk(path)
        # заводим цикл для проверки всех путей в исходной папке
        for directory in dirs:
            # первый элемент в списке-элементе, возвращённом os.path - это путь до папки
            normpath = os.path.normpath(directory[0])
            # переключаемся на директорию из списка. Без явого перключения Ubuntu ичего не делает.
            os.chdir(normpath)
            # если среди файлов в директории есть запрошенный нами файл - прерываем цикл, так как мы уже в нужной
            # директории
            if self.file_name in directory[2]:
                break
            else:
                # если нет, проверяем, нет ли в папке архивов
                for file in directory[2]:
                    # если архив есть, открываем его на чтение и проверяем содержимое
                    if zipfile.is_zipfile(file):
                        archive = zipfile.ZipFile(file, "r")
                        content = archive.namelist()
                        # если файл есть в архиве, то раззиповываем его и прерываем цикл обхода папок
                        if self.file_name in content:
                            archive.extract(self.file_name)
                            break
        print("Запрашиваемый файл не найден в данной директории или вложенных.")

    def count_letters(self):
        # TODO тут пишем условие если self.file_name имеет окончание .zip

        # TODO А если мы его уже после предыдущего теста раззиповали?..
        # TODO Почему не работать сразу с именем конечного файла, который нам нужен?
        if str(self.file_name).endswith(".txt"):
            self.find_file_directory()
            with open(self.file_name, "r", encoding="cp1251") as file:
                for line in file:
                    self.check_symbols(line)
            self.sort_statistics()
            self.print_result()

    def sort_statistics(self):
        sorted(self.statistics)

    def check_symbols(self, line):
        for char in line:
            if char.isalpha():
                if char in self.statistics:
                    self.statistics[char] = self.statistics[char] + 1
                else:
                    self.statistics[char] = 1
                self.letters_total += 1

    def print_result(self):
        print("""+---------+----------+
|  буква  | частота  |
+---------+----------+""")
        for key in self.statistics:
            value = self.statistics[key]
            print("|{:^9}|{:^10}|".format(key, value))
        print("+---------+----------+")
        print("|{:^9}|{:^10}|".format("Итого", self.letters_total))
        print("+---------+----------+")


test = InOutBlock(file_name="voyna-i-mir.txt")
test.count_letters()


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
