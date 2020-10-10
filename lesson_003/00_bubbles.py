# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint as rd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    # TODO за место (255, 148, 60) используем константы из библиотеки sd
    sd.circle(point, radius=radius, color = (255, 148, 60), width=2)
    radius += 5

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO steps_amount можно не передовать
def bubble (point, step, steps_amount, color):
    radius = 50
    # TODO тут делаем range 3
    for _ in range(steps_amount):
        sd.circle(point, radius=radius, color=color)
        radius += step

# Нарисовать 10 пузырьков в ряд

# TODO получать x будем цикле фор заведем range от 100 до 1000 с шагом 100
# TODO внутри функции вызовем нашу функцию которую написали выши
x = 100
for _ in range (10):
    point = sd.get_point(x, 200)
    radius = 50
    for _ in range (5):
        sd.circle(point, radius=radius, color = (225, 135, 225), width = 3)
        radius += 10
    x += 100

# Нарисовать три ряда по 10 пузырьков

# TODO аналогично тут X Y будем получать в циклах, у нас их будет два
# TODO внутри крайнего получим точку и вызовем нашу функцию bubble
# TODO за место rd используем функцию из sd random_point
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

# TODO используем в цикле for функцию bubble с нужными параметрами
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
