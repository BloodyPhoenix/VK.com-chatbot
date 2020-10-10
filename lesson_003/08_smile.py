# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as draw
from random import randint as random

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile (x, y, color):
    center = draw.get_point(x, y)
    draw.circle(center, color=color, width=0, radius=30)
    left_eye_down = draw.get_point(x-15, y)
    left_eye_up = draw.get_point(x-5, y+15)
    right_eye_down = draw.get_point(x+5, y)
    right_eye_up = draw.get_point(x+15, y+15)
    draw.ellipse(left_eye_down, left_eye_up, (0, 0, 0), 0)
    draw.ellipse(right_eye_down, right_eye_up, (0, 0, 0), 0)
    start1 = draw.get_point(x-15, y-10)
    fin1start2 = draw.get_point(x+10, y-10)
    draw.line(start1, fin1start2, (0, 0, 0), 2)
    fin2 = draw.get_point(x+20, y-5)
    draw.line(fin1start2, fin2, (0, 0, 0), 2)


for _ in range(10):
    x = random(30, 560)
    y = random(30, 560)
    color = (random(0, 225), random(0, 225), random(0, 225))
    smile(x, y, color)


draw.pause()

# зачет!
