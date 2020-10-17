# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint as random

sd.resolution = (1000, 1000)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def blossom_tree(point, angle, length, delta=30):
    if length < 1:
        return
    if isinstance(point, sd.Point):
        start_point = point
    else:
        start_point = sd.get_point(*point)
    if 1 < length < 2:
        if random(1, 10) == 10:
            color = sd.COLOR_RED
        elif random(1, 10) == 5:
            color = (255, 255, 255)
        else:
            color = sd.COLOR_GREEN
    else:
        color = sd.COLOR_YELLOW
    branch = sd.get_vector(start_point=start_point, angle=angle, length=length)
    branch.draw(color=color, width=3)
    next_point = branch.end_point
    next_angle = angle - delta
    next_length = length * .75
    blossom_tree(point=next_point, angle=next_angle, length=next_length, delta=delta)
    blossom_tree(point=next_point, angle=next_angle + delta * 2, length=next_length, delta=delta)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def blossom_tree_update(point, angle, length, dispersion=30):
    if length < 1:
        return
    if isinstance(point, sd.Point):
        start_point = point
    else:
        start_point = sd.get_point(*point)
        # А что, если рисование начинаем не от низа экрана?
        if start_point.y > 0:
            x = sd.resolution[0]*.5
            sd.line(sd.get_point(x, 0), start_point, width=3)
    if 1 < length < 2:
        if random(1, 10) == 10:
            color = sd.COLOR_RED
        elif random(1, 10) == 5:
            color = (255, 255, 255)
        else:
            color = sd.COLOR_GREEN
    elif 2 <= length < 5:
        color = sd.COLOR_GREEN
    else:
        color = sd.COLOR_YELLOW

    branch = sd.get_vector(start_point=start_point, angle=angle, length=length)
    branch.draw(color=color, width=3)
    next_point = branch.end_point
    next_angle = angle - dispersion + sd.random_number(-6, 6)
    next_length = length * (.75 + sd.random_number(-10, 10) * 0.01)
    blossom_tree_update(point=next_point, angle=next_angle, length=next_length, dispersion=dispersion)
    blossom_tree_update(point=next_point, angle=next_angle + dispersion * 2, length=next_length, dispersion=dispersion)


blossom_tree_update((450, 150), 60, 100)
# Мне кажется, с двумя векторами и одним вызовом рекурсии функция отрабатывала быстрее...
sd.pause()

# Прекрасное дерево!

# зачет!
