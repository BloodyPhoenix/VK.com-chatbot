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
        # TODO Добавим необязательный аргумент в виде пути до папки, откуда будем искать
        if path:
            self.path = os.path.normpath(file_path)
        # TODO Если там ничего нет - ищем от директории, где запустили скрипт
        else:
            self.path = os.getcwd()

    def find_file_directory(self):
        # получаем список директорий и поддиректорий в ней
        # тут мы получаем не dirs а dirpath, dirnames, filenames сразу три параметра
        # незабываем что переменные пишутся в стиле snake_case
        # TODO тут мы три параметра получить не можем, так как os.walk возвращает итерируемый объект типа generator
        # TODO который содержит свежения о текущей папке и всех вложенных
        # TODO из него перебором в цикле можно вытащить путь до каждой папки (первый элемент в элементе генератора),
        # TODO список вложенных папок (второй элемент) и список файлов (третий)
        # TODO кстати, первый элемент в генераторе - это корень, откуда запущен скрипт, так что его мы тоже проверяем
        dirs = os.walk(self.path)
        # заводим цикл для проверки всех путей в исходной папке
        for directory in dirs:
            # первый элемент в списке-элементе, возвращённом os.path - это путь до папки
            normpath = os.path.normpath(directory[0])
            for file in directory[2]:
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
        # TODO тут пишем условие если self.file_name имеет окончание .zip
        # TODO Зачем, если мы при поиске файла в директории его уже раззиповали?
        # TODO self.file_name и так строка зачем ее еще раз преобразовывать
        # TODO потому что иначе ПайЧарм ругается
        if str(self.file_name).endswith(".txt"):
            # TODO зачем запускать файл если он может лежать в корне! Нужно делать проверку
            #TODO Проверка с помощью os.walk идёт от корня. См. комментарии выше.
            if self.find_file_directory():
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
