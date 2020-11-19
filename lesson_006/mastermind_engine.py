# -*- coding: utf-8 -*-

from random import randint as random

_secret_number = []


def guess_number():
    global _secret_number
    while True:
        _secret_number = random(1000, 9999)
        _secret_number = str(_secret_number)
        if len(set(_secret_number)) == 4:
            print(_secret_number)
            break


def check_user_number(user_number):
    for symbol in user_number:
        if symbol.isdigit() is False:
            return False, "Вы ввели не число! Повторите ввод."

    if "0" == user_number[0]:
        return False, "Первая цифра - ноль! Повторите ввод."
    elif len(user_number) < 4:
        return False, "Вы ввели меньше четырёх цифр! Повторите ввод."
    elif len(user_number) > 4:
        return False, "Вы ввели больше четырёх цифр! Повторите ввод."
    elif len(set(user_number)) < 4:
        return False, "Вы ввели одну и ту же цифру дважды! Повторите ввод."
    else:
        return True, None


def counting_bulls_and_cows(user_number):
    bulls_and_cows = {"bulls": 0, "cows": 0}
    win = False
    for number in range(0, 4):
        if _secret_number[number] == user_number[number]:
            bulls_and_cows["bulls"] = bulls_and_cows["bulls"] + 1
        elif user_number[number] in _secret_number:
            bulls_and_cows["cows"] = bulls_and_cows["cows"] + 1
    if bulls_and_cows["bulls"] == 4:
        win = True
    return win, bulls_and_cows


def new_game():
    counter = 0
    guess_number()
    return counter
