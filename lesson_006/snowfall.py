# -*- coding: utf-8 -*-

import simple_draw as sd


_snowflakes = []


def create_snowflakes(number):
    global _snowflakes
    max_x = sd.resolution[0] - 100
    max_y = sd.resolution[1] + 200
    min_y = sd.resolution[1] + 100

    for _ in range(number):
        x = sd.random_number(100, max_x)
        y = sd.random_number(min_y, max_y)
        lengh = sd.random_number(10, 100)
        _snowflakes.append([x, y, lengh])

# TODO используйте константы цвета из библиотеке
def draw_snowflakes(color=(255, 255, 255)):
    global _snowflakes
    # TODO в range можно писать без первого аргумента 0, поправить везде
    for i in range(0, len(_snowflakes)):
        snowflake_x = _snowflakes[i][0]
        snowflake_y = _snowflakes[i][1]
        snowflake_length = _snowflakes[i][2]
        center = sd.get_point(snowflake_x, snowflake_y)
        sd.snowflake(center=center, length=snowflake_length, color=color)


def move_snowflakes():
    global _snowflakes
    draw_snowflakes(sd.background_color)
    for i in range(0, len(_snowflakes)):
        snowflake_x = _snowflakes[i][0]
        snowflake_y = _snowflakes[i][1]
        snowflake_x += sd.random_number(-30, 30)
        snowflake_y -= 10
        _snowflakes[i][0] = snowflake_x
        _snowflakes[i][1] = snowflake_y


def fallen_flakes_numbers():
    # TODO если мы не изменяем _snowflakes в коде то глобал можно не использовать!
    global _snowflakes
    fallen_flakes = []
    # TODO используйте enumerate для получения индекса и самого объекта снежинка
    for i in range (0, len(_snowflakes)):
        snowflake_y = _snowflakes[i][1]
        snowflake_lenght = _snowflakes[i][2]
        if snowflake_y < 0-(snowflake_lenght)*2:
            fallen_flakes.append(i)
    return fallen_flakes

# TODO алгоритм примерно такой:
# TODO указываем что список снежинок у нас глобальный
# TODO проходимся по списку индексов и получаем именно индексы
# TODO то удаляем данную снежинку по индексу из списка

# TODO иногда снежинки зависают для того чтобы это не происходило нужно
#  отсортировать список snowflakes_remove и повернуть его! до того как с ним работать в методе fallen_flakes_numbers

def delete_snowflakes(snowflakes_numbers):
    global _snowflakes
    for i in range(0, len(_snowflakes)):
        if i in snowflakes_numbers:
            snowflake_x = _snowflakes[i][0]
            snowflake_y = _snowflakes[i][1]
            snowflake_length = _snowflakes[i][2]
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length, color=sd.background_color)
            del _snowflakes[i]

