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
    for i, snowflake in enumerate(_snowflakes):
        if snowflake[1] < 0 - snowflake[2] * 2:
            fallen_flakes.append(i)
    return fallen_flakes


def delete_snowflakes(snowflakes_numbers):
    snowflakes_numbers = snowflakes_numbers[::-1]
    for i in (snowflakes_numbers):
        del _snowflakes[i]
