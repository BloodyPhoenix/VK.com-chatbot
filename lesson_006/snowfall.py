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
    # TODO если мы не изменяем список _snowflakes то глобал можно не указывать он ее возьмет сам из глобального
    # TODO скоупа
    global _snowflakes
        for i in range(len(_snowflakes)):
            # TODO съехал таб
        snowflake_x = _snowflakes[i][0]
        snowflake_y = _snowflakes[i][1]
        snowflake_length = _snowflakes[i][2]
        center = sd.get_point(snowflake_x, snowflake_y)
        sd.snowflake(center=center, length=snowflake_length, color=color)


def move_snowflakes():
    global _snowflakes
    draw_snowflakes(sd.background_color)
    # TODO первый 0 можно не указывать! Поправить ниже по коду
    for i in range(0, len(_snowflakes)):
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
    for i in range (0, len(_snowflakes)):
        snowflake_y = _snowflakes[i][1]
        snowflake_lenght = _snowflakes[i][2]
        if snowflake_y < 0-(snowflake_lenght)*2:
            fallen_flakes.append(i)
    return fallen_flakes



# TODO для того чтобы удалять снежинки по индексам вам нужно
# TODO в цикле получить те самые индексы, но предварительно список fallen_flakes отсортировать и перевернуть
# TODO Как только получили индекс по нему можно сразу удалить снежинку из списка _snowflakes
# TODO останется решить проблему как и где обнулить fallen_flakes
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

