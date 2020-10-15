# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_triangle(start_point, angle, side_length):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(sd.COLOR_DARK_ORANGE, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle+120, side_length)
    side_2.draw(sd.COLOR_DARK_ORANGE, width=3)
    sd.line(side_2.end_point, point_1, sd.COLOR_DARK_ORANGE, width=3)

draw_triangle((100, 100), 20, 200)

def draw_square(start_point, angle, side_length):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(sd.COLOR_PURPLE, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle + 90, side_length)
    side_2.draw(sd.COLOR_PURPLE, width=3)
    side_3 = sd.get_vector(side_2.end_point, angle + 180, side_length)
    side_3.draw(sd.COLOR_PURPLE, width=3)
    sd.line(side_3.end_point, point_1, sd.COLOR_PURPLE, width=3)

draw_square((300,300), 50, 150)

def draw_pentagon(start_point, angle, side_length):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(sd.COLOR_PURPLE, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle + 180-108, side_length)
    side_2.draw(sd.COLOR_PURPLE, width=3)
    side_3 = sd.get_vector(side_2.end_point, angle + (180-108)*2, side_length)
    side_3.draw(sd.COLOR_PURPLE, width=3)
    side_4 = sd.get_vector(side_3.end_point, angle + (180-108)*3, side_length)
    side_4.draw(sd.COLOR_PURPLE, width=3)
    side_5.draw(sd.COLOR_PURPLE, width=3)
    sd.line(side_4.end_point, point_1, sd.COLOR_PURPLE, width=3)

draw_pentagon((100,400), 50, 50)

def draw_hexagon(start_point, angle, side_length):
    point_1 = sd.get_point(*start_point)
    side_1 = sd.get_vector(point_1, angle, side_length)
    side_1.draw(sd.COLOR_DARK_RED, width=3)
    side_2 = sd.get_vector(side_1.end_point, angle + 180-120, side_length)
    side_2.draw(sd.COLOR_DARK_RED, width=3)
    side_3 = sd.get_vector(side_2.end_point, angle + (180-120)*2, side_length)
    side_3.draw(sd.COLOR_DARK_RED, width=3)
    side_4 = sd.get_vector(side_3.end_point, angle + (180-120)*3, side_length)
    side_4.draw(sd.COLOR_DARK_RED, width=3)
    side_5 = sd.get_vector(side_4.end_point, angle + (180-120)*4, side_length)
    side_5.draw(sd.COLOR_DARK_RED, width=3)
    sd.line(side_5.end_point, point_1, sd.COLOR_DARK_RED, width=3)


draw_hexagon((300, 400), 50, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
