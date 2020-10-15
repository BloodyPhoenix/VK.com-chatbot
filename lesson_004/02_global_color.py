# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

COLOR_LIST = (sd.COLOR_RED, sd.COLOR_ORANGE,  sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
              sd.COLOR_PURPLE)
print("""Введите число от 1 до 7, чтобы выбрать цвет.
1 - красный
2 - оранжевый
3 - жёлтый
4 - зелёный
5 - голубой
6 - синий
7 - фиолетовый""")
while True:
    chosen_color = input()
    if chosen_color.isdigit():
        if 0< int(chosen_color) <8:
            break
        else:
            print("Вы ввели неверное число! Повторите ввод.")
            print()
            continue
    else:
        print("Вы ввели не целое число. Повторите ввод.")
        print()
        continue

chosen_color = COLOR_LIST[int(chosen_color)-1]

def draw_triangle(start_point, angle, side_length, color):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(color=color, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle+120, side_length)
    side_2.draw(color=color, width=3)
    sd.line(side_2.end_point, point_1, color=color, width=3)

def draw_square(start_point, angle, side_length, color):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(color=color, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle + 90, side_length)
    side_2.draw(color=color, width=3)
    side_3 = sd.get_vector(side_2.end_point, angle + 180, side_length)
    side_3.draw(color=color, width=3)
    sd.line(side_3.end_point, point_1, color=color, width=3)

def draw_pentagon(start_point, angle, side_length, color):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(color=color, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle + 180-108, side_length)
    side_2.draw(color=color, width=3)
    side_3 = sd.get_vector(side_2.end_point, angle + (180-108)*2, side_length)
    side_3.draw(color=color, width=3)
    side_4 = sd.get_vector(side_3.end_point, angle + (180-108)*3, side_length)
    side_4.draw(color=color, width=3)
    sd.line(side_4.end_point, point_1, color=color, width=3)

def draw_hexagon(start_point, angle, side_length, color):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(color=color, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle + 180-120, side_length)
    side_2.draw(color=color, width=3)
    side_3 = sd.get_vector(side_2.end_point, angle + (180-120)*2, side_length)
    side_3.draw(color=color, width=3)
    side_4 = sd.get_vector(side_3.end_point, angle + (180-120)*3, side_length)
    side_4.draw(color=color, width=3)
    side_5 = sd.get_vector(side_4.end_point, angle + (180-120)*4, side_length)
    side_5.draw(color=color, width=3)
    sd.line(side_5.end_point, point_1, color=color, width=3)

draw_triangle(start_point=(100, 100), angle = 0, side_length=100, color=chosen_color)
draw_square(start_point=(100, 400), angle = 0, side_length=100, color=chosen_color)
draw_pentagon(start_point=(400, 400), angle = 0, side_length=100, color=chosen_color)
draw_hexagon(start_point=(400, 100), angle = 0, side_length=100, color=chosen_color)

sd.pause()
