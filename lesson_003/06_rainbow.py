# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (600, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# TODO нейминг переменных их лучше назвать вот так x_start
xstart, ystart, xfinal, yfinal = 50, 50, 350, 450
step = 5
width = 4

# TODO тут мы в цикле будем получать color из тьюпла rainbow_colors, так сразу и напишем!
for i in range(0, len(rainbow_colors)):
    start_point = sd.get_point(xstart, ystart)
    final_point = sd.get_point(xfinal, yfinal)
    sd.line(start_point, final_point, rainbow_colors[i], width)
    ystart -= step
    yfinal -= step


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

center = sd.get_point(300, -45)
radius = 330
# TODO аналогично получаем color! скобки нужно убрать, пайчарм вам подсказывает
for i in (rainbow_colors):
    sd.circle(center, radius, i, width)
    radius -= step



sd.pause()
