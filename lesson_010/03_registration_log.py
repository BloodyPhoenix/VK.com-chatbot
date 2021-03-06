# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os
import zipfile


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class CheckRegistrations:

    def __init__(self, file_name, path=None):
        if not path:
            self.path = os.getcwd()
        else:
            self.path = path
        self.file_name = file_name
        self.line = None

    def find_file(self):
        dirs = os.walk(self.path)
        for dir_path, _, filenames in dirs:
            normpath = os.path.normpath(dir_path)
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

    def check_registrations(self):
        if self.find_file():
            with open(self.file_name, "r") as registrations:
                line_number = 0
                for line in registrations.readlines():
                    line_number += 1
                    self.line = line
                    try:
                        self.check_line()
                    except ValueError as exc:
                        self.bad_log(exc, line_number)
                    except NotNameError as exc:
                        self.bad_log(exc, line_number)
                    except NotEmailError as exc:
                        self.bad_log(exc, line_number)
                    finally:
                        self.write_log()

    def check_line(self):
        line_data = self.line.split()
        if len(line_data) != 3:
            raise ValueError("Присутствуют не все поля")
        name, email, age = line_data
        if age.isalpha():
            raise ValueError("Возраст не является числом")
        if 10 >= int(age) >= 100:
            raise ValueError("Некореектный возраст")
        if not name.isalpha():
            raise NotNameError("Некорректное поле имени")
        if "@" not in email:
            raise NotEmailError("Некорректный емейл: не хватает знака\"@\"")
        if "." not in email:
            raise NotEmailError("Некорректный емейл: не хватает точки")

    def bad_log(self, exc, line_number):
        message = f"Ошибка: {exc} в строке {line_number}\n"
        self.line = message

    def write_log(self):
        if "Ошибка" in self.line:
            with open("registrations_bad.log", "a") as bad_log:
                bad_log.write(self.line)
        else:
            with open("registrations_good.log", "a") as good_log:
                good_log.write(self.line)


check = CheckRegistrations("registrations.txt")
check.check_registrations()
