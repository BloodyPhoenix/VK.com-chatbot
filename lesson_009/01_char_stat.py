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


class InOutBlock:

    def __init__(self, file_name):
        self.file_name = file_name
        self.statistics = {}
        self.letters_total = 0
        # TODO заведем параметр self.base_path который будет равнять полному папки от куда был запущен скрипт
        # TODO используя os.path.dirname(__file__)
        # TODO далее мы сформируем путь до директории где лежит файл с помощью os.path.join
        # TODO следующей строкой осталось только подставить self.file_name то же можно с помощью join
        # TODO на выходу у вас полный путь до файла в 3-4 строки


    # TODO в основном эти два мейджик метода нужны для того чтобы создать совой кастомный контестный метод
    # TODO https://python-scripts.com/contextlib
    # TODO в данном случае нам они не нужны тут
    def __enter__(self):
        return self

    def __exit__(self):
        return

    # TODO мы знаем что файл лежит в python_snippets так давай его от туда возьмем без этих танцев с бубнами
    # TODO сразу при инициализации зададим нужный путь до него

    # TODO тут пишем метод который распаковывает архив
    # TODO и переопределяет self.file_name

    @staticmethod
    def find_file_directory(file_name):
        # получаем текущую рабочую директорию
        path = os.getcwd()
        # получаем список директорий и поддиректорий в ней
        dirs = os.walk(path)
        # заводим цикл для проверки всех путей в исходной папке
        for directory in dirs:
            # первый элемент в списке-элементе, возвращённом os.path - это путь до папки
            normpath = os.path.normpath(directory[0])
            # переключаемся на директорию из списка.Без явого перключения Ubuntu ичего не делает.
            os.chdir(normpath)
            # если среди файлов в директории есть запрошенный нами файл - прерываем цикл, так как мы уже в нужной
            # директории
            if file_name in directory[2]:
                break
            else:
                # если нет, проверяем, нет ли в папке архивов
                for file in directory[2]:
                    # если архив есть, открываем его на чтение и проверяем содержимое
                    if zipfile.is_zipfile(file):
                        archive = zipfile.ZipFile(file, "r")
                        content = archive.namelist()
                        # если файл есть в архиве, то раззиповываем его и прерываем цикл обхода папок
                        if file_name in content:
                            archive.extract(file_name)
                            break

    def count_letters(self):
        # TODO тут пишем условие если self.file_name имеет окончание .zip
        # TODO то вызываем метод self.unzip() - который распаковывает его
        # TODO к методам класса обращаемся через self
        InOutBlock.find_file_directory(self.file_name)
        with open(self.file_name, "r", encoding="cp1251") as file:
            for line in file:
                self.check_symbols(line)
        sorted(self.statistics)
        self.print_result()

    # TODO также часть кода нужно выделить в отдельный метод который отвечает за сортировку словаря
    # TODO это нужно для дальнейшей доработки

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
