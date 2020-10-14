 # -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    sd.circle(point, radius=radius, color = sd.COLOR_DARK_ORANGE, width=2)
    radius += 5


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble (point, step, color):
    radius = 50
    for _ in range(3):
        sd.circle(point, radius=radius, color=color)
        radius += step


# Нарисовать 10 пузырьков в ряд
for x in range (100, 1001, 100):
     point = sd.get_point(x, 200)
     bubble(point, 5, sd.COLOR_DARK_PURPLE)

# Нарисовать три ряда по 10 пузырьков

for y in range (400, 550, 50):
    for x in range (100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point, 5, sd.COLOR_DARK_RED)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubble(point, 5, color)


sd.pause()

# зачет!
