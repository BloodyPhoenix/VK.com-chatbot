# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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

print("""Выберите фигуру, которую хотите нарисовать.
3 - треугольник
4 - квадрат
5 - пятугольник
6 - шестиугольник""")

while True:
    chosen_shape = input()
    if chosen_shape.isdigit():
        if 2 < int(chosen_shape) < 7:
            break
        else:
            print("Вы указали неверный номер фигуры. Пожалуйста, повторите ввод.")
            # Принт для отступа, ятобы было красивее
            print()
            continue
    else:
        print("Вы ввели не целое число. Повторите ввод.")
        print()
        continue


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
    sd.line(side_5.end_point, point_1, color=color, width=3)_point, angle + (180 - 120) * 5, side_length)

shapes = (draw_triangle, draw_square, draw_pentagon, draw_hexagon)
chosen_shape = int(chosen_shape)-3

shapes[chosen_shape]((250, 250), 0, 100, chosen_color)


sd.pause()
