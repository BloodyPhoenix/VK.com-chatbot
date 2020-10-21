# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


COLORS_AVALIBLE = {
    1: ("красный", sd.COLOR_RED),
    2: ("оранжевый", sd.COLOR_ORANGE),
    3: ("жёлтый", sd.COLOR_YELLOW),
    4: ("зелёный", sd.COLOR_GREEN),
    5: ("голубой", sd.COLOR_CYAN),
    6: ("синий", sd.COLOR_BLUE),
    7: ("фиолетовый", sd.COLOR_PURPLE)
}

print("Введите число от 1 до 7, чтобы выбрать цвет.")
for number in range(1, len(COLORS_AVALIBLE) + 1):
    print(f"{number} - {COLORS_AVALIBLE[number][0]}")

while True:
    chosen_color = input()
    if chosen_color.isdigit():
        chosen_color = int(chosen_color)
        if chosen_color in COLORS_AVALIBLE:
            chosen_color_code = COLORS_AVALIBLE[chosen_color][1]
        break
    else:
        print("Вы ввели неверное число! Повторите ввод.")
        print()

shapes = {
    3: ("треугольник", draw_triangle),
    4: ("квадрат", draw_square),
    5: ("пятиугольник", draw_pentagon),
    6: ("шестиугольник", draw_hexagon)
}

print("Выберите фигуру, которую хотите нарисовать.")
# Если мы предполагаем расширение списка, то получаем тут такое замечательное уродство, так как предлагаем
# сделать выбор, начиная с тройки (по кол-ву углов/сторон)
for number in range(3, len(shapes) + 3):
    print(f"{number} - {shapes[number][0]}")

while True:
    chosen_shape = input()
    if chosen_shape.isdigit():
        chosen_shape = int(chosen_shape)
        if chosen_shape in shapes:
            # TODO chosen_color_code нужно объявить в глобальном скоупе! Пайчар ругается
            shapes[chosen_shape][1]((250, 250), 0, 100, chosen_color_code)
            break
        else:
            print("Вы ввели неверный номер фигуры. Пожалуйста, повторите ввод.")
    else:
        print("Вы указали неверный номер фигуры. Пожалуйста, повторите ввод.")
        # Принт для отступа, чтобы было красивее
        print()

sd.pause()
