# -*- coding: utf-8 -*-

import simple_draw as sd
import snow

def rainbow():

    import simple_draw as sd

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    step = 5
    width = 4

    y = sd.resolution[1]*.5

    center = sd.get_point(y, -45)
    radius = 330
    for colors in rainbow_colors:
        sd.circle(center, radius, colors, width)
        radius -= step

    sd.pause()

def animated_rainbow(start_color=0):

    import simple_draw as sd

    sd.resolution = (600, 600)
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    step = 5
    width = 4

    y = sd.resolution[1] * .5

    center = sd.get_point(y, -45)
    radius = 330
    for color in range (start_color, len(rainbow_colors)+start_color):
        color_number = color%len(rainbow_colors)
        sd.circle(center, radius, rainbow_colors[color_number], width)
        radius -= step


number = 0

while True:
    animated_rainbow(number)
    for _ in range (10):
        snow.snowfall(20)
    number -= 1
    sd.sleep(1)
    if sd.user_want_exit():
        break

sd.pause()





