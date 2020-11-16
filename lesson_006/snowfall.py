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
    # TODO можно было записать вот так:
    # for index, snowflake in enumerate(_snowflakes):
    #     if snowflake[1] < 0:
    #         fallen_flakes.append(index)

    # Нет. Потому что, если мы проверяем первое от снежинки без её длины, умноденной на два, она удаляется раньше,
    # чем долетает до конца экрана. Теоретически может быть запись
    # for index, snowflake in enumerate(_snowflakes):
    # if snowflake[1] < 0-snowflake[2]*2:
    #         fallen_flakes.append(index)
    # Я просто предпочла явное именование переменных координаты y  и длины снежинки, чтобы было понятно, что тут
    # происходит. В таком варианте я не виду никакого смысла применять enumerate, так как будет то же самое, только
    # ещё добавится переменная snowflake

    for i in range (len(_snowflakes)):
        snowflake_y = _snowflakes[i][1]
        snowflake_lenght = _snowflakes[i][2]
        if snowflake_y < 0-(snowflake_lenght)*2:
            fallen_flakes.append(i)
    return fallen_flakes



# TODO для того чтобы удалять снежинки по индексам вам нужно
# TODO в цикле получить те самые индексы, но предварительно список fallen_flakes отсортировать и перевернуть

# Зачем его переворачивать, если он УЖЕ содержит индексы? От того, что я его переверну, значения индексов не изменятся.
# счёт обнуления fallen_flakes - он пересчитывается заново при отрисовке каждого кажра, зачем его обнулять?

def delete_snowflakes(snowflakes_numbers):
    global _snowflakes
    for i in range(0, len(_snowflakes)):
        if i in snowflakes_numbers:
            snowflake_x = _snowflakes[i][0]
            snowflake_y = _snowflakes[i][1]
            snowflake_length = _snowflakes[i][2]
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length, color=sd.background_color)
            del _snowflakes[i]

