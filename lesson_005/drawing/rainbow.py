# -*- coding: utf-8 -*-


def rainbow(start_color=0, rainbow_delta=0.5):

    import simple_draw as sd

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    step = 5
    width = 4
    x = sd.resolution[0] * rainbow_delta

    center = sd.get_point(x, 0)
    radius = sd.resolution[1] - 100
    sd.start_drawing()
    for color in range (start_color, len(rainbow_colors)+start_color):
        color_number = color%len(rainbow_colors)
        sd.circle(center, radius, rainbow_colors[color_number], width)
        radius -= step




def animated_rainbow():
    import simple_draw as draw
    while True:
        for color in range (0, 7):
            if draw.user_want_exit():
                break
            rainbow(color)
            draw.sleep(1)
        if draw.user_want_exit():
            break
    draw.pause()








