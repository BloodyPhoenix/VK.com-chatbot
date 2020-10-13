# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as draw
from random import randint as random


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for row, y in enumerate(range(0, 601, 50)):
    if row % 2 == 0:
        zero_point = 0
    else:
        zero_point = -50
    for x in range(zero_point, 601, 100):
        start_point = draw.get_point(x, y)
        final_point = draw.get_point(x+100, y+50)
        color = (random(0, 225), random(0, 225), random(0, 225))
        draw.rectangle(start_point, final_point, color)

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

# Прекрасно!

# зачет!
