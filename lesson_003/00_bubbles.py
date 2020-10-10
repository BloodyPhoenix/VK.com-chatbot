# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint as rd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    sd.circle(point, radius=radius, color = (255, 148, 60), width=2)
    radius += 5

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble (point, step, steps_amount, color):
    radius = 50
    for _ in range(steps_amount):
        sd.circle(point, radius=radius, color=color)
        radius += step

# Нарисовать 10 пузырьков в ряд
x = 100
for _ in range (10):
    point = sd.get_point(x, 200)
    radius = 50
    for _ in range (5):
        sd.circle(point, radius=radius, color = (225, 135, 225), width = 3)
        radius += 10
    x += 100

# Нарисовать три ряда по 10 пузырьков

y = 500
for _ in range (3):
    x = 100
    for _ in range (10):
        point = sd.get_point(x, y)
        radius = 50
        for _ in range (2):
            sd.circle(point, radius=radius, color = (75, 225, 75), width = 3)
            radius += 10
        x += 100
    y -= 50

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    y = rd(0, 599)
    x = rd (0, 1199)
    point = sd.get_point(x, y)
    color = (rd(0, 225), rd (0, 225), rd (0, 225))
    radius = 20
    for _ in range (5):
        sd.circle(point, radius, color)
        radius += 3


sd.pause()
