# -*- coding: utf-8 -*

def blossom_tree(point, angle, length, dispersion=30):

    import simple_draw as sd
    from random import randint as random

    if length < 1:
        return
    if isinstance(point, sd.Point):
        start_point = point
    else:
        start_point = sd.get_point(*point)
    if 1 < length < 2:
        if random(1, 10) == 10:
            color = sd.COLOR_RED
        elif random(1, 10) == 5:
            color = (255, 255, 255)
        else:
            color = sd.COLOR_DARK_GREEN
    elif 2 <= length < 5:
        color = sd.COLOR_DARK_GREEN
    else:
        color = sd.COLOR_DARK_YELLOW

    branch = sd.get_vector(start_point=start_point, angle=angle, length=length)
    branch.draw(color=color, width=3)
    next_point = branch.end_point
    next_angle = angle - dispersion + sd.random_number(-6, 6)
    next_length = length * (.75 + sd.random_number(-10, 10) * 0.01)
    blossom_tree(point=next_point, angle=next_angle, length=next_length, dispersion=dispersion)
    blossom_tree(point=next_point, angle=next_angle + dispersion * 2, length=next_length, dispersion=dispersion)
