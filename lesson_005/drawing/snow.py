# -*- coding: utf-8 -*-

import simple_draw as sd


def snowdrift(N=20, base_height=0, max_x=1200):

    min_x = 0
    start_y = sd.resolution[1]+200
    snowflakes = []
    fallen_snowflakes = []
    snowdrift_height = base_height

    for _ in range(N):
        x = sd.random_number(min_x, max_x)
        y = start_y
        lenght = sd.random_number(10, 50)
        snowflakes.append([x, y, lenght])

    while len(fallen_snowflakes) <= N*10:
        for i in range(N):
            snowflake_x = snowflakes[i][0]
            snowflake_y = snowflakes[i][1]
            snowflake_length = snowflakes[i][2]
            snowflake_x += sd.random_number(-10, 10)
            snowflake_y -= 10
            snowflakes[i][0] = snowflake_x
            snowflakes[i][1] = snowflake_y
            if snowflake_y <= snowdrift_height:
                fallen_snowflakes.append((snowflake_x, snowflake_y, snowflake_length))
                if len(fallen_snowflakes) % N == 0:
                    snowdrift_height += 10
                min_x += 1
                max_x -= 1
                snowflakes[i][0] = sd.random_number(min_x, max_x)
                snowflakes[i][1] = start_y
    return fallen_snowflakes

def draw_snowdrift(fallen_snowflakes):
    for flake in fallen_snowflakes:
        flake_center = sd.get_point(flake[0], flake[1])
        sd.snowflake(flake_center, flake[2])


def start_snowfall(N=20):
    max_x = sd.resolution[0] - 100
    max_y = sd.resolution[1] + 200
    min_y = sd.resolution[1] + 100
    snowflakes = []

    for _ in range(N):
        x = sd.random_number(100, max_x)
        y = sd.random_number(min_y, max_y)
        lenght = sd.random_number(10, 100)
        snowflakes.append([x, y, lenght])

    return snowflakes


def snowfall(snowflakes=0):

    if snowflakes == 0:
        snowflakes = start_snowfall()

    for i in range(0, len(snowflakes)):
        snowflake_x = snowflakes[i][0]
        snowflake_y = snowflakes[i][1]
        snowflake_length = snowflakes[i][2]
        center = sd.get_point(snowflake_x, snowflake_y)
        sd.snowflake(center=center, length=snowflake_length)
        snowflake_x += sd.random_number(-30, 30)
        snowflake_y -= 10
        snowflakes[i][0] = snowflake_x
        snowflakes[i][1] = snowflake_y

    return snowflakes



