# -*- coding: utf-8 -*-

def sun(beam_1_lengh=25):

    import simple_draw as sd

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

def animated_sun ():

    import simple_draw as sd

    color = sd.COLOR_YELLOW
    center = sd.get_point(sd.resolution[0]-150, sd.resolution[1]-150)
    angle = 0
    step = 360 / 12
    beam_1_lenth = 25
    beams = []
    while True:
        beam_1_lenth += 5
        if beam_1_lenth > 55:
            beam_1_lenth = 25
        sd.start_drawing()
        if len(beams) > 0:
            for vectors in beams:
                vectors[0].draw(color=sd.background_color)
                vectors[1].draw(color=sd.background_color)
            beams = []
            sd.circle(center_position=center, color=color, radius=25, width=0)
        for _ in range (12):
            beam_1 = sd.get_vector(center, angle, length=beam_1_lenth)
            beam_1.draw(color)
            vector = sd.get_vector(beam_1.end_point, angle, 10)
            beam_2 = sd.get_vector(vector.end_point, angle, 45-beam_1_lenth)
            beam_2.draw(color)
            angle += step
            beams.append((beam_1, beam_2))
        if sd.user_want_exit():
            break
        sd.finish_drawing()
        sd.sleep(0.1)
    sd.pause()

