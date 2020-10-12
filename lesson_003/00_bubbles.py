 # -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint as rd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    sd.circle(point, radius=radius, color = sd.COLOR_DARK_ORANGE, width=2)
    radius += 5

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble (point, step, color):
    radius = 50
    for _ in range(3):
        sd.circle(point, radius=radius, color=color)
        radius += step

# Нарисовать 10 пузырьков в ряд
for x in range (100, 1001, 100):
     point = sd.get_point(x, 200)
     for _ in range (5):
         bubble(point, 5, sd.COLOR_DARK_PURPLE)
     x += 100

# Нарисовать три ряда по 10 пузырьков

for y in range (400, 550, 50):
    for x in range (100, 1001, 100):
        point = sd.get_point(x, y)
        for _ in range(5):
            bubble(point, 5, sd.COLOR_DARK_RED)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    y = rd(0, 599)
    x = rd (0, 1199)
    point = sd.get_point(x, y)
    color = (rd(0, 225), rd (0, 225), rd (0, 225))
    for _ in range (5):
        bubble(point, 5, color)



sd.pause()
