# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import choice, randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class CarmaError(Exception):

    def __init__(self, mistake):
        self.mistake = mistake

    def __str__(self):
        return self.mistake


class IamGodError(CarmaError):
    def __init__(self, mistake="Возомнил себя богом"):
        super().__init__(mistake)


class DrunkError(CarmaError):
    def __init__(self, mistake="Надрался как свинья"):
        super().__init__(mistake)


class CarCrashError(CarmaError):
    def __init__(self, mistake="Разбился на машине"):
        super().__init__(mistake)


class GluttonyError(CarmaError):
    def __init__(self, mistake="Обожрался как свинья"):
        super().__init__(mistake)


class DepressionError(CarmaError):
    def __init__(self, mistake="Впал в уныние"):
        super().__init__(mistake)


class SuicideError(CarmaError):
    def __init__(self, mistake="Суициднулся"):
        super().__init__(mistake)


EXCEPTIONS = (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError)


def one_day():
    global tries
    tries += 1
    mistake_chance = randint(1, 13)
    if mistake_chance == 13:
        try:
            exc = choice(EXCEPTIONS)
            raise exc()
        except CarmaError as exc:
            raise exc
    else:
        return randint(1, 7)


def write_log(exception, tries):
    log_message = f"Произошла ошибка класса {exception} на попытке номер {tries} \n"
    with open("groundhog day.log", "a") as log:
        log.write(log_message)


# TODO сделать это оригинальнее через методы os.path вне функции
# TODO А зачем?
log = open("groundhog day.log", "w")
log.close()
carma = 0
tries = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        carma += one_day()
    except CarmaError as exc:
        write_log(exc, tries)

# https://goo.gl/JnsDqu
