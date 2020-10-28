# -*- coding: utf-8 -*-

def draw_shape(start_point, start_angle, side_length, sides, color = (0, 0, 0)):

    import simple_draw as sd

    if start_point is tuple:
        start_point = sd.get_point(*start_point)

    point_1 = start_point
    step = 360 / sides
    for n in range(0, sides - 1):
        side = sd.get_vector(start_point, start_angle + step * n, side_length)
        side.draw(color, width=3)
        start_point = side.end_point
    sd.line(point_1, start_point, color, width=3)

def draw_triangle(start_point, side_length, start_angle=0, color = (0, 0, 0)):
    draw_shape(start_point, start_angle, side_length, color=color, sides=3)


def draw_square(start_point, side_length, start_angle=0, color = (0, 0, 0)):
    draw_shape(start_point, start_angle, side_length, color=color, sides=4)


def draw_pentagon(start_point, side_length, start_angle=0, color = (0, 0, 0)):
    draw_shape(start_point, start_angle, side_length, color=color, sides=5)


def draw_hexagon(start_point, side_length, start_angle=0, color = (0, 0, 0)):
    draw_shape(start_point, start_angle, side_length, color = color, sides=6)

