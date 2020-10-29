# -*- coding: utf-8 -*-

def draw_shape(start_point, start_angle, side_length, sides, color = (0, 0, 0), width=3):

    import simple_draw as sd

    if start_point is tuple:
        start_point = sd.get_point(*start_point)

    point_1 = start_point
    step = 360 / sides
    for n in range(0, sides - 1):
        side = sd.get_vector(start_point, start_angle + step * n, side_length)
        side.draw(color, width=width)
        start_point = side.end_point
    sd.line(point_1, start_point, color, width=width)

def draw_triangle(start_point, side_length, start_angle=0, color = (0, 0, 0), width=3):
    draw_shape(start_point, start_angle, side_length, width, color=color, sides=3, width=3)


def draw_square(start_point, side_length, start_angle=0, color = (0, 0, 0), width=3):
    draw_shape(start_point, start_angle, side_length, width=3, color=color, sides=4)


def draw_pentagon(start_point, side_length, start_angle=0, color = (0, 0, 0), width=3):
    draw_shape(start_point, start_angle, side_length, width, color=color, sides=5, width=3)


def draw_hexagon(start_point, side_length, start_angle=0, color = (0, 0, 0), width=3):
    draw_shape(start_point, start_angle, side_length, width, color = color, sides=6, width=3)

def smile_open_eyes (x, y, color):
    import  simple_draw as draw

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


def smile_closed_eyes (x, y, color):
    import  simple_draw as draw

    center = draw.get_point(x, y)
    draw.circle(center, color=color, width=0, radius=30)
    left_eye_down = draw.get_point(x-15, y)
    left_eye_up = draw.get_point(x-5, y)
    right_eye_down = draw.get_point(x+5, y)
    right_eye_up = draw.get_point(x+15, y)
    draw.ellipse(left_eye_down, left_eye_up, (0, 0, 0), 0)
    draw.ellipse(right_eye_down, right_eye_up, (0, 0, 0), 0)
    start1 = draw.get_point(x-15, y-10)
    fin1start2 = draw.get_point(x+10, y-10)
    draw.line(start1, fin1start2, (0, 0, 0), 2)
    fin2 = draw.get_point(x+20, y-5)
    draw.line(fin1start2, fin2, (0, 0, 0), 2)

