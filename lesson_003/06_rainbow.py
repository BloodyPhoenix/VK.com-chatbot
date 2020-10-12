# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (600, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x_start, y_start, x_final, y_final = 50, 50, 350, 450
step = 5
width = 4

for colors in rainbow_colors:
    start_point = sd.get_point(x_start, y_start)
    final_point = sd.get_point(x_final, y_final)
    sd.line(start_point, final_point, colors, width)
    y_start -= step
    y_final -= step


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

center = sd.get_point(300, -45)
radius = 330
for colors in rainbow_colors:
    sd.circle(center, radius, colors, width)
    radius -= step



sd.pause()
