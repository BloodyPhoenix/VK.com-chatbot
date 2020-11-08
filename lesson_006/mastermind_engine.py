# -*- coding: utf-8 -*-

from random import randint as random

_secret_number = []


def guess_number():
    # TODO Можно упростить заводим бесконечный цикл
    # TODO final_result присваиваем строку в которой randint(1000, 9999)
    # TODO Потом проверяем если set этой строки без дублей, (и прочекать длину)
    # TODO то выходим из цикла
    # TODO и возвращаем нужный нам результат
    global _secret_number
    if len(_secret_number) > 0:
        _secret_number = []
    while True:
        number = random(1, 9)
        if number not in _secret_number:
            _secret_number.append(number)
            if len(_secret_number) == 4:
                break
    return None

# TODO вот тут как раз пишем функцию проверки которая наружу будет выдавать True\False
# TODO нам нужен отдельный метод который чекает число пользователя на ошибки,
# TODO Можно создать список булевых значений и чекать его сразу в if функцией all, будет один if!
# TODO У вас должно быть 4 проверки: на число, на длинну, на длинну set, и на первый 0, только в нужном порядке!

# TODO разделить эту функцию на две
def counting_bulls_and_cows(user_number):
    bulls_and_cows = {"bulls": 0, "cows": 0}
    if len(user_number) < 4:
        return "less_than_four"
    elif len(user_number) > 4:
        return "more_than_four"

    for symbol in user_number:
        if symbol.isdigit() is False:
            return "value_error"

    user_number = [int(n) for n in user_number]
    if 0 in user_number:
        return "zero_in_list"
    elif len(set(user_number)) < 4:
        return "double_value"

    for _ in range(0, 4):
        if _secret_number[_] == user_number[_]:
            bulls_and_cows["bulls"] = bulls_and_cows["bulls"] + 1
        elif user_number[_] in _secret_number:
            bulls_and_cows["cows"] = bulls_and_cows["cows"] + 1

    if bulls_and_cows["bulls"] == 4:
        return "win"
    else:
        return bulls_and_cows
