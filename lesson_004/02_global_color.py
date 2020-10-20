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

def draw_triangle(start_point, start_angle, side_length, color, sides=3):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    step = 360 / sides
    for n in range(0, sides - 1):
        side = sd.get_vector(start_point, start_angle + step * n, side_length)
        side.draw(color, width=3)
        start_point = side.end_point
    sd.line(point_1, start_point, color, width=3)


def draw_square(start_point, start_angle, side_length, color, sides=4):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    step = 360 / sides
    for n in range(0, sides - 1):
        side = sd.get_vector(start_point, start_angle + step * n, side_length)
        side.draw(color, width=3)
        start_point = side.end_point
    sd.line(point_1, start_point, color, width=3)


def draw_pentagon(start_point, start_angle, side_length, color, sides=5):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    step = 360 / sides
    for n in range(0, sides - 1):
        side = sd.get_vector(start_point, start_angle + step * n, side_length)
        side.draw(color, width=3)
        start_point = side.end_point
    sd.line(point_1, start_point, color, width=3)


def draw_hexagon(start_point, start_angle, side_length, color, sides=6):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    step = 360 / sides
    for n in range(0, sides - 1):
        side = sd.get_vector(start_point, start_angle + step * n, side_length)
        side.draw(color, width=3)
        start_point = side.end_point
    sd.line(point_1, start_point, color, width=3)


# Честно говоря, я бы делала через список кортежей, чтобы спокойно ссылаться на индексы, а не на ключи, раз уж мы всё
# равно работаем с жёстко нумерованным упорядоченным списком

COLORS_AVALIBLE = {
    1: ("красный", sd.COLOR_RED),
    2: ("оранжевый", sd.COLOR_ORANGE),
    3: ("жёлтый", sd.COLOR_YELLOW),
    4: ("зелёный", sd.COLOR_GREEN),
    5: ("голубой", sd.COLOR_CYAN),
    6: ("синий", sd.COLOR_BLUE),
    7: ("фиолетовый", sd.COLOR_PURPLE)
}

# А здесь бы тогда был enumerate от COLORS_AVALIBLE. Конструкция вида COLORS_AVALIBLE[number][0] тоже не особо читаема
# Если мы предполагаем расширение списка, то нам тут нужно ещё и проверять его длину, причём прибалять к ней 1.
# Очень понятный код...
print("Введите число от 1 до 7, чтобы выбрать цвет.")
for number in range(1, len(COLORS_AVALIBLE) + 1):
    print(f"{number} - {COLORS_AVALIBLE[number][0]}")

while True:
    chosen_color = input()
    if chosen_color.isdigit():
        chosen_color = int(chosen_color)
        if chosen_color in COLORS_AVALIBLE:
            chosen_color_code = COLORS_AVALIBLE[chosen_color][1]
            draw_triangle(start_point=(100, 100), start_angle=0, side_length=100, color=chosen_color_code)
            draw_square(start_point=(100, 400), start_angle=0, side_length=100, color=chosen_color_code)
            draw_pentagon(start_point=(400, 400), start_angle=0, side_length=100, color=chosen_color_code)
            draw_hexagon(start_point=(400, 100), start_angle=0, side_length=100, color=chosen_color_code)
            break
        else:
            print("Вы ввели неверное число! Повторите ввод.")
            print()
    else:
        print("Вы ввели не целое число. Повторите ввод.")
        print()
        continue

# Альтернативный вариант через список кортежей. Да, чуть больше переменных, зато более адекватная итерация по циклу

# COLORS_AVALIBLE = [
#     ("красный", sd.COLOR_RED),
#     ("оранжевый", sd.COLOR_ORANGE),
#     ("жёлтый", sd.COLOR_YELLOW),
#     ("зелёный", sd.COLOR_GREEN),
#     ("голубой", sd.COLOR_CYAN),
#     ("синий", sd.COLOR_BLUE),
#     ("фиолетовый", sd.COLOR_PURPLE)
# ]

# print("Введите число от 1 до 7, чтобы выбрать цвет.")
# for number, color in enumerate(COLORS_AVALIBLE):
#     real_number = number + 1
#     color_name = color[0]
#     print(f"{real_number} - {color_name}")
#
# while True:
#     try:
#         chosen_color = int(input())
#     except:
#         print("Вы ввели не целое число. Повторите ввод.")
#         print()
#         continue
#     chosen_color -= 1
#     if 0< chosen_color < len(COLORS_AVALIBLE):
#         chosen_color_code = COLORS_AVALIBLE[chosen_color][1]
#         draw_triangle(start_point=(100, 100), start_angle=0, side_length=100, color=chosen_color_code)
#         draw_square(start_point=(100, 400), start_angle=0, side_length=100, color=chosen_color_code)
#         draw_pentagon(start_point=(400, 400), start_angle=0, side_length=100, color=chosen_color_code)
#         draw_hexagon(start_point=(400, 100), start_angle=0, side_length=100, color=chosen_color_code)
#         break
#     else:
#         print("Вы ввели неверное число! Повторите ввод.")
#         print()
#         continue

sd.pause()
