# -*- coding: utf-8 -*

import simple_draw as draw
from random import randint as random


def blossom_tree(point, angle, length, dispersion=30):
    if length < 1:
        return
    if isinstance(point, draw.Point):
        start_point = point
    else:
        start_point = draw.get_point(*point)
    if 1 < length < 2:
        if random(1, 10) == 10:
            color = draw.COLOR_RED
        elif random(1, 10) == 5:
            color = (255, 255, 255)
        else:
            color = draw.COLOR_DARK_GREEN
    elif 2 <= length < 5:
        color = draw.COLOR_DARK_GREEN
    else:
        color = draw.COLOR_DARK_YELLOW

    branch = draw.get_vector(start_point=start_point, angle=angle, length=length)
    branch.draw(color=color, width=3)
    next_point = branch.end_point
    next_angle = angle - dispersion + draw.random_number(-6, 6)
    next_length = length * (.75 + draw.random_number(-10, 10) * 0.01)
    blossom_tree(point=next_point, angle=next_angle, length=next_length, dispersion=dispersion)
    blossom_tree(point=next_point, angle=next_angle + dispersion * 2, length=next_length, dispersion=dispersion)


def three_trees_scenery():
    draw.start_drawing()
    first_tree_x = int(draw.resolution[0] * .75)
    first_tree_y = int(draw.resolution[1] * .25)
    first_tree_start = draw.get_point(first_tree_x, first_tree_y)
    blossom_tree(first_tree_start, 90, 75)
    second_tree_x = int(draw.resolution[0] * .95)
    second_tree_y = int(draw.resolution[1] * .2)
    second_tree_start = draw.get_point(second_tree_x, second_tree_y)
    blossom_tree(second_tree_start, 90, 100)
    third_tree_x = int(draw.resolution[0] * .85)
    third_tree_y = int(draw.resolution[1] * .15)
    third_tree_start = draw.get_point(third_tree_x, third_tree_y)
    blossom_tree(third_tree_start, 90, 65)
    draw.finish_drawing()


def two_trees_scenery():
    draw.start_drawing()
    first_tree_start_x = int(draw.resolution[0]) * .75
    first_tree_start_y = int(draw.resolution[1] * .25)
    first_tree_start = draw.get_point(first_tree_start_x, first_tree_start_y)
    second_tree_start_x = int(draw.resolution[0] * .85)
    second_tree_start_y = first_tree_start_y
    blossom_tree(first_tree_start, 90, 100)
    second_tree_start = draw.get_point(second_tree_start_x, second_tree_start_y)
    blossom_tree(second_tree_start, 90, 75)
    draw.finish_drawing()
