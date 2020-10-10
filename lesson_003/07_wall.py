# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as draw
from random import randint as random


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x = 0
for x in range (0, 601, 100):
    y = 0
    xfinal = x + 100
    for y in range (0, 601, 50):
        start_point = draw.get_point(x, y)
        y += 50
        final_point = draw.get_point(xfinal, y)
        color = (random(0, 225), random(0, 225), random(0, 225))
        draw.rectangle(start_point, final_point, color)
    x += 100

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

draw.pause()
