# -*- coding: utf-8 -*-

from random import randint as random

_secret_number = []


def guess_number():
    global _secret_number
    while True:
        _secret_number = random(1000, 9999)
        _secret_number = str(_secret_number)
        if len(set(_secret_number)) == 4:
            break
    print(_secret_number)


# TODO Данном модуле мы учимся разделять блоки кода на отдельные части и писать под каждую часть свою функцию
# TODO Стремимся к тому что функции должны отвечать за чтото одно, код должен быть краткий и четкий.
# TODO Если видим что вложенность или сильно длинная функция то стараемся ее разбить на модули блоки(функции)

# TODO Посмотрим на эту функцию из главного модуля где не видно весь код что тут внутри, функция у вас называется
# TODO подсчет быков и кором, логически подумать от куда тут может взяться код на валидацию числа от пользователя
# TODO на корректность? Правильно, для этого я вас просил разбит данную функцию на две,
# TODO Каждая функция это у нас логические блоки, в данном случае у явные два блока, два этапа действий
def counting_bulls_and_cows(user_number):
    if len(user_number) < 4:
        return False, "Вы ввели меньше четырёх цифр! Повторите ввод."
    elif len(user_number) > 4:
        return False, "Вы ввели больше четырёх цифр! Повторите ввод."

    for symbol in user_number:
        if symbol.isdigit() is False:
            return False, "Вы ввели не число! Повторите ввод."

    if "0" == user_number[0]:
        return False, "Первая цифра - ноль! Повторите ввод."
    elif len(set(user_number)) < 4:
        return False, "Вы ввели одну и ту же цифру дважды! Повторите ввод."
    else:
        bulls_and_cows = {"bulls": 0, "cows": 0}
        # TODO Если в коде переменная используется то ей нужно дать имя! знак _ используется когда переменная не нужна
        for _ in range(0, 4):
            if _secret_number[_] == user_number[_]:
                bulls_and_cows["bulls"] = bulls_and_cows["bulls"] + 1
            elif user_number[_] in _secret_number:
                bulls_and_cows["cows"] = bulls_and_cows["cows"] + 1
        if bulls_and_cows["bulls"] == 4:
            return True, "win"
        else:
            return True, bulls_and_cows
