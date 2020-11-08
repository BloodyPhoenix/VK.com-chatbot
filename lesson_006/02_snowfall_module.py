# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

import simple_draw as sd
from snowfall import create_snowflakes, draw_snowflakes, move_snowflakes, fallen_flakes_numbers, delete_snowflakes

create_snowflakes(20)
sd.set_screen_size(1200, 600)
while True:
    sd.start_drawing()
    draw_snowflakes(sd.background_color)
    move_snowflakes()
    # TODO используем константы цвета из библиотеке
    draw_snowflakes(color=(255, 255, 255))
    fallen_flakes = fallen_flakes_numbers()
    # TODO тут можно написать просто if fallen_flakes:
    if len(fallen_flakes) > 0:
        delete_snowflakes(fallen_flakes)
        create_snowflakes(len(fallen_flakes))
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
