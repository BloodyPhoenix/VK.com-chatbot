# -*- coding: utf-8 -*-

import simple_draw as sd


_snowflakes = []


def create_snowflakes(number):
    global _snowflakes
    max_x = sd.resolution[0] - 100
    max_y = sd.resolution[1] + 200
    min_y = sd.resolution[1] + 100

    for _ in range(number):
        x = sd.random_number(100, max_x)
        y = sd.random_number(min_y, max_y)
        lengh = sd.random_number(10, 100)
        _snowflakes.append([x, y, lengh])


def draw_snowflakes(color=sd.COLOR_WHITE):
    for i in range(len(_snowflakes)):
        snowflake_x = _snowflakes[i][0]
        snowflake_y = _snowflakes[i][1]
        snowflake_length = _snowflakes[i][2]
        center = sd.get_point(snowflake_x, snowflake_y)
        sd.snowflake(center=center, length=snowflake_length, color=color)


def move_snowflakes():
    global _snowflakes
    draw_snowflakes(sd.background_color)
    for i in range(len(_snowflakes)):
        snowflake_x = _snowflakes[i][0]
        snowflake_y = _snowflakes[i][1]
        snowflake_x += sd.random_number(-30, 30)
        snowflake_y -= 10
        _snowflakes[i][0] = snowflake_x
        _snowflakes[i][1] = snowflake_y


def fallen_flakes_numbers():
    fallen_flakes = []
    # TODO почему в большей части нужно делать так, это более питонический подход
    # TODO Посмотрите статью по этому поводу.
    # TODO https://habr.com/ru/company/ruvds/blog/485648/

    for i in range(len(_snowflakes)):
        snowflake_y = _snowflakes[i][1]
        snowflake_lenght = _snowflakes[i][2]
        # TODO для удобочитаемости 0-(snowflake_lenght)*2 вынесете в отдельную переменную, скобки не нужны!
        if snowflake_y < 0-(snowflake_lenght)*2:
            fallen_flakes.append(i)
    return fallen_flakes


# Зачем его переворачивать, если он УЖЕ содержит индексы? От того, что я его переверну, значения индексов не изменятся.
# TODO чтобы удаление было с конца, допустим у нас список [5, 9] если мы удалим индекс 5, длинна сместиться
# TODO и 9 индекса уже не будет!
# счёт обнуления fallen_flakes - он пересчитывается заново при отрисовке каждого кажра, зачем его обнулять?
# TODO Хорошо давайте посмотрим как будет работать скрипт с этими изменениями.


def delete_snowflakes(snowflakes_numbers):
    global _snowflakes
    # TODO исправить, писал вам про это в прошлых туду про 0
    for i in range(0, len(_snowflakes)):
        if i in snowflakes_numbers:
            # TODO отрисовывать тут мы ничего не должны, только удаляем! Может быть по этому сразу было не видно
            # TODO что происходит с снежинками если список не перевернуть
            snowflake_x = _snowflakes[i][0]
            snowflake_y = _snowflakes[i][1]
            snowflake_length = _snowflakes[i][2]
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length, color=sd.background_color)
            del _snowflakes[i]

