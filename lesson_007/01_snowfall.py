# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.y = sd.random_number(sd.resolution[1] + 100, sd.resolution[1] + 200)
        self.x = sd.random_number(100, sd.resolution[0] - 100)
        self.lenght = sd.random_number(20, 50)
        self.center = sd.get_point(self.x, self.y)

    def clear_previous_picture(self):
        sd.snowflake(self.center, self.lenght, color=sd.background_color)

    def move(self):
        if self.can_fall():
            self.y -= 15
            self.x += sd.random_number(-10, 10)

    def draw(self):
        self.center = sd.get_point(self.x, self.y)
        sd.snowflake(self.center, self.lenght)

    def can_fall(self):
        return self.y >= 0 - self.lenght


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

_flakes = []


def get_flakes(count):
    for _ in range(count):
        _flakes.append(Snowflake())


def get_fallen_flakes():
    fallen_flakes = 0
    for i, flake in enumerate(flakes):
        if not flake.can_fall():
            del flakes[i]
            fallen_flakes += 1
    return fallen_flakes


def append_flakes(fallen_flakes):
    get_flakes(fallen_flakes)


get_flakes(20)
while True:
    sd.start_drawing()
    for flake in _flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(fallen_flakes)  # добавить еще сверху
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
