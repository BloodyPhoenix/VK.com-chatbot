# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    sides = n

    def draw_shape(point, angle, length):
        point_1 = point
        start_point = point
        step = 360 / sides
        for side in range(sides-1):
            side = sd.get_vector(start_point, angle + step * side, length)
            side.draw(sd.COLOR_DARK_ORANGE, width=3)
            start_point = side.end_point
        # Конец дорисовывается таким образом, чтобы обеспечить точное замыкание которого не дают векторы
        sd.line(point_1, start_point, sd.COLOR_DARK_ORANGE, width=3)

    return draw_shape


draw_triangle = get_polygon(n=6)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()

# зачет!
