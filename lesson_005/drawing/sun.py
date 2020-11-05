# -*- coding: utf-8 -*-

import simple_draw as sd

def sun(beam_1_lengh=25):

    color = sd.COLOR_YELLOW
    center = sd.get_point(50, sd.resolution[1]-50)
    sd.circle(center_position=center, color=color, radius=25, width=0)
    beams = []
    angle = 0
    step = 360/12
    for _ in range(12):
        beam_1 = sd.get_vector(center, angle, length=beam_1_lengh)
        beam_1.draw(color)
        vector = sd.get_vector(beam_1.end_point, angle, 10)
        beam_2 = sd.get_vector(vector.end_point, angle, 45 - beam_1_lengh)
        beam_2.draw(color)
        angle += step
        beams.append((beam_1, beam_2))
    return beams, center

def animated_sun(beam_1_lenght=25):

    color = sd.COLOR_YELLOW
    center = sd.get_point(int(sd.resolution[0]*.2), sd.resolution[1]-150)
    angle = 0
    step = 360 / 12
    sd.circle(center_position=center, color=color, radius=25, width=0)
    for _ in range(12):
        beam_1 = sd.get_vector(center, angle, length=beam_1_lenght)
        beam_1.draw(color)
        vector = sd.get_vector(beam_1.end_point, angle, 10)
        beam_2 = sd.get_vector(vector.end_point, angle, 45 - beam_1_lenght)
        beam_2.draw(color)
        angle += step
    beam_1_lenght += 5

    return beam_1_lenght



