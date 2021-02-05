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


class InOutBlock:

    def __init__(self, file_name, path=None):
        self.file_name = file_name
        self.statistics = {}
        self.letters_total = 0
        self.sort_keys = []
        self.sort_by_alphabet = True

        if path:
            self.path = os.path.normpath(file_name)
        else:
            self.path = os.getcwd()

    def find_file_directory(self):
        dirs = os.walk(self.path)
        # заводим цикл для проверки всех путей в исходной папке
        for dirpath, _, filenames in dirs:
            # первый элемент в списке-элементе, возвращённом os.path - это путь до папки
            normpath = os.path.normpath(dirpath)
            for file in filenames:
                if self.check_file_name(file):
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

    def count_letters(self):
        if self.file_name.endswith(".txt"):
            if self.find_file_directory():
                with open(self.file_name, "r", encoding="cp1251") as file:
                    for line in file:
                        self.check_symbols(line)
                self.sort_statistics()
                self.print_result()

    def sort_statistics(self):
        for letter in self.statistics:
            self.sort_keys.append(self.statistics[letter])
        self.sort_keys.sort(reverse=True)
        self.sort_by_alphabet = False

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
        if self.sort_by_alphabet:
            for sort_key in self.sort_keys:
                value = self.statistics[sort_key]
                print("|{:^9}|{:^10}|".format(sort_key, value))
        else:
            for sort_key in self.sort_keys:
                for key, value in self.statistics.items():
                    if sort_key == value:
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


class AscFrequencySort(InOutBlock):

    # TODO метод инит писать не обязательно мы в нем ничего не переопределяем!
    def __init__(self, file_name, path=None):
        super().__init__(file_name, path)

    def sort_statistics(self):
        for letter in self.statistics:
            self.sort_keys.append(self.statistics[letter])
        self.sort_keys.sort()
        self.sort_by_alphabet = False


class AscAlphabetSort(InOutBlock):

    def __init__(self, file_name, path=None):
        super().__init__(file_name, path)

    def sort_statistics(self):
        for letter in self.statistics:
            self.sort_keys.append(letter)
        self.sort_keys.sort(reverse=True)
        self.sort_by_alphabet = True


class DescAlphabetSort(InOutBlock):

    def __init__(self, file_name, path=None):
        super().__init__(file_name, path)

    def sort_statistics(self):
        for letter in self.statistics:
            self.sort_keys.append(letter)
        self.sort_keys.sort()
        self.sort_by_alphabet = True


test = AscFrequencySort(file_name="voyna-i-mir.txt")
test.count_letters()
test = AscAlphabetSort(file_name="voyna-i-mir.txt")
test.count_letters()
test = DescAlphabetSort(file_name="voyna-i-mir.txt")
test.count_letters()


