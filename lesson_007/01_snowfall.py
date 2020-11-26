# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    fallen_flakes = 0
    flakes = []
    count=20

    def get_flakes():
        for _ in range(Snowflake.count):
            Snowflake.flakes.append(Snowflake())

    def get_fallen_flakes():
        for i, flake in enumerate(Snowflake.flakes):
            if not flake.can_fall():
                del Snowflake.flakes[i]
                Snowflake.fallen_flakes += 1


    def append_flakes():
        Snowflake.count = Snowflake.fallen_flakes
        Snowflake.get_flakes()
        Snowflake.fallen_flakes = 0

    def __init__(self):
        max_x = sd.resolution[0] - 100
        max_y = sd.resolution[1] + 200
        min_y = sd.resolution[1] + 100
        self.y = sd.random_number(min_y, max_y)
        self.x = sd.random_number(100, max_x)
        self.lenght = sd.random_number(20, 50)
        self.center = sd.get_point(self.x, self.y)

    def clear_previous_picture(self):
        sd.snowflake(self.center, self.lenght, color=sd.background_color)

    def move(self):
        self.y -= 15
        self.x += sd.random_number(-10, 10)
        self.center = sd.get_point(self.x, self.y)

    def draw(self):
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

Snowflake.get_flakes()
while True:
    sd.start_drawing()
    for flake in Snowflake.flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    Snowflake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if Snowflake.fallen_flakes:
        Snowflake.append_flakes()  # добавить еще сверху
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
