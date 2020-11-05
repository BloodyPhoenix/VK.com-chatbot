# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

import simple_draw as draw
from drawing import rainbow, snow, sun, tree, house



draw.set_screen_size(1500, 1000)

# Статичная картинка
# draw.start_drawing()
# sun.sun()
# rainbow.rainbow(rainbow_delta=1)
# house.field()
# tree.three_trees_scenery()
# snow.draw_snowdrift(snow.snowdrift(base_height=190, max_x=450))
# house.house()
# draw.finish_drawing()

# Анимированная картинка

tree.two_trees_scenery()
draw.take_background()
animation_counter = 0
rainbow_counter = 0
left_snowdrift = snow.snowdrift(base_height=190, max_x=450)
front_snowdrift = snow.snowdrift(base_height=10, max_x=1500)
beam_1_lenght = 25
falling_flakes = 0
while True:
    draw.start_drawing()
    draw.draw_background()
    rainbow.rainbow(start_color=rainbow_counter, rainbow_delta=1)
    house.field()
    beam_1_lenght = sun.animated_sun(beam_1_lenght)
    if beam_1_lenght > 55:
        beam_1_lenght = 25
    if animation_counter % 10 == 0 or animation_counter % 11 == 0 or animation_counter % 12 == 0:
        house.house(blink=1)
    else:
        house.house(blink=0)
    snow.draw_snowdrift(left_snowdrift)
    snow.draw_snowdrift(front_snowdrift)
    if animation_counter < 1:
        falling_flakes = snow.snowfall()
    else:
        falling_flakes = snow.snowfall(falling_flakes)
    animation_counter += 1
    if animation_counter > 120:
        animation_counter = 0
    if animation_counter % 4 == 0:
        rainbow_counter += 1
        if rainbow_counter > 6:
            rainbow_counter = 0
    draw.finish_drawing()
    draw.sleep(0.1)

    if draw.user_want_exit():
        break

draw.pause()