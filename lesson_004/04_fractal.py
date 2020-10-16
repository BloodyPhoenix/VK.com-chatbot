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

# TODO во всех функциях нужно использовать только один вектор и две внутренние рекурсии!

def blossom_tree(point, angle, length, base_angle=90):
    if length < 1:
        return
    if isinstance(point, sd.Point):
        start_point = point
    else:
        start_point = sd.get_point(*point)
        sd.line(sd.get_point(300, 0), start_point, color=sd.COLOR_YELLOW, width=2)
    if 1<length<2:
        if random(1, 10) == 10:
            color = sd.COLOR_RED
        elif random(1, 10) == 5:
            color = (255, 255, 255)
        else:
            color = sd.COLOR_GREEN
    else:
        color = sd.COLOR_YELLOW
    branch_angle = angle*0.5
    branch_1 = sd.get_vector(start_point, base_angle-branch_angle, length, 2)
    branch_1.draw(color=color)
    branch_2 = sd.get_vector(start_point, base_angle + branch_angle, length, 2)
    branch_2.draw(color=color)
    next_length = length*0.75
    next_point_1= branch_1.end_point
    next_base_angle_1 = base_angle-branch_angle
    next_point_2 = branch_2.end_point
    next_base_angle_2 = base_angle+branch_angle
    blossom_tree(point=next_point_1, angle=angle, length=next_length, base_angle=next_base_angle_1)
    blossom_tree(point=next_point_2, angle=angle, length=next_length, base_angle=next_base_angle_2)






# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def blossom_tree_update(point, angle, length, base_angle=90):
    if length < 1:
        return
    if isinstance(point, sd.Point):
        start_point = point
    else:
        start_point = sd.get_point(*point)
        sd.line(sd.get_point(300, 0), start_point, color=sd.COLOR_YELLOW, width=3)
    if 1<length<2:
        if random(1, 10) == 10:
            color = sd.COLOR_RED
        elif random(1, 10) == 5:
            color = (255, 255, 255)
        else:
            color = sd.COLOR_GREEN
    elif 2<=length<5:
        color = sd.COLOR_GREEN
    else:
        color = sd.COLOR_YELLOW
    branch_angle = angle*0.5
    branch_1 = sd.get_vector(start_point, base_angle-branch_angle, length, 2)
    branch_1.draw(color=color)
    branch_2 = sd.get_vector(start_point, base_angle + branch_angle, length, 2)
    branch_2.draw(color=color)
    next_length = length*(0.75+sd.random_number(-10, 10)*0.01)
    next_point_1= branch_1.end_point
    next_base_angle_1 = base_angle-branch_angle+sd.random_number(-6,6)
    next_point_2 = branch_2.end_point
    next_base_angle_2 = base_angle+branch_angle+sd.random_number(-6,6)
    blossom_tree_update(point=next_point_1, angle=angle, length=next_length, base_angle=next_base_angle_1)
    blossom_tree_update(point=next_point_2, angle=angle, length=next_length, base_angle=next_base_angle_2)

blossom_tree_update((450, 200), 60, 100)

sd.pause()
