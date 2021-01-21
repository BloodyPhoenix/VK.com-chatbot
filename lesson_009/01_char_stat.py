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

    def __enter__(self):
        return self

    def __exit__(self):
        return

    @staticmethod
    # TODO Да, это обязательный метод, потому что без смены рабочей директории под Убунтой ничего не работает
    def find_file_directory(file_name):
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
    def count_letters(file_name):
        InOutBlock.find_file_directory(file_name)
        letters_counter = {"total": 0}
        with open(file_name, "r", encoding="cp1251") as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in letters_counter:
                            letters_counter[char] = letters_counter[char]+1
                            letters_counter["total"] = letters_counter["total"]+1
                        else:
                            letters_counter[char] = 1
        InOutBlock.print_result(letters_counter)

    @staticmethod
    def print_result(result):
        print("""+---------+----------+
|  буква  | частота  |
+---------+----------+""")
        for key in result:
            if len(key) < 2:
                value = result[key]
                print("|{:^9}|{:^10}|".format(key, value))
        print("+---------+----------+")
        value = result["total"]
        print("|{:^9}|{:^10}|".format("Итого", value))
        print("+---------+----------+")


test = InOutBlock()
test.count_letters(file_name="voyna-i-mir.txt")


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
