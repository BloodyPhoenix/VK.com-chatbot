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

# TODO как вы написали все эти "заморочки" для расширения кода, без лишнего переписывания
# TODO и удобного обращения к атрибутам в нутри одного объекта


class InOutBlock:

    def __init__(self, file_name):
        self.file_name = file_name
        self.statistics = {}
        self.letters_total = 0
    # TODO Честно говоря, всё равно не поняла, зачем тут обязательно нужен класс, если можно обойтись без него
    # TODO Но, возможно, дело в том, что я просто больше люблю функциональный стиль программирования и чего-то
    # TODO не понимаю. Не вижу, как в данном случае наличие класса упрощает жизнь, и всё тут.

    # TODO для чего нам эти два класса ?
    # TODO В лекции преподаватель говорил, что без них ничего работать не будет, так как они означают вход
    # TODO в блок кода и выход из него
    def __enter__(self):
        return self

    def __exit__(self):
        return

    # Да, это обязательный метод, потому что без смены рабочей директории под Убунтой ничего не работает
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
        InOutBlock.find_file_directory(self.file_name)
        with open(self.file_name, "r", encoding="cp1251") as file:
            for line in file:
                self.check_symbols(line)
        sorted(self.statistics)
        self.print_result()

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
