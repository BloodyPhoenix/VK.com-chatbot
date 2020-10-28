# -*- coding: utf-8 -*-

def snowdrift(N=20, base_height=0, max_x=1200):

    import simple_draw as sd

    min_x = 0
    start_y = sd.resolution[1]+200
    snowflakes = []
    fallen_snowflakes = []
    snowdrift_height = base_height

    for _ in range(N):
        x = sd.random_number(min_x, max_x)
        y = start_y
        lengh = sd.random_number(10, 50)
        snowflakes.append([x, y, lengh])

    while len(fallen_snowflakes) <= N*10:
        for i in range(N):
            snowflake_x = snowflakes[i][0]
            snowflake_y = snowflakes[i][1]
            snowflake_length = snowflakes[i][2]
            snowflake_x += sd.random_number(-10, 10)
            snowflake_y -= 10
            snowflakes[i][0] = snowflake_x
            snowflakes[i][1] = snowflake_y
            if snowflake_y <= snowdrift_height:
                fallen_snowflakes.append((snowflake_x, snowflake_y, snowflake_length))
                if snowdrift_height == N*10:
                    snowdrift_height = 10
                elif len(fallen_snowflakes) % N == 0:
                    snowdrift_height += 10
                min_x += 1
                max_x -= 1
                snowflakes[i][0] = sd.random_number(min_x, max_x)
                snowflakes[i][1] = start_y

    return fallen_snowflakes


def snowfall(N=20):

    import simple_draw as sd

    max_x = sd.resolution[0] - 100
    max_y = sd.resolution[1] + 200
    min_y = sd.resolution[1] + 100
    snowflakes = []

    for _ in range(N):
        x = sd.random_number(100, max_x)
        y = sd.random_number(min_y, max_y)
        lengh = sd.random_number(10, 100)
        snowflakes.append([x, y, lengh])

    fallen_snowflakes = []
    snowdrift_height = 0

    while True:
        sd.start_drawing()
        for i in range(N):
            snowflake_x = snowflakes[i][0]
            snowflake_y = snowflakes[i][1]
            snowflake_length = snowflakes[i][2]
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length, color=sd.background_color)
            snowflake_x += sd.random_number(-30, 30)
            snowflake_y -= 10
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length)
            snowflakes[i][0] = snowflake_x
            snowflakes[i][1] = snowflake_y
            if snowflake_y <= snowdrift_height:
                # Используем список для повторной отрисовки, чтобы не возникало артефактов от падаюих сверху снежинок
                # Параметры снежинок записываем кортежем, так как они уже не поменяются
                fallen_snowflakes.append((snowflake_x, snowflake_y, snowflake_length))
                # Сохраняем проверку на кол-во упавших снежинок, чтобы сугроб не рос бесконечно
                if len(fallen_snowflakes) > 200:
                    del fallen_snowflakes[0]
                # Когда пора убирать старые снежинки, сбрасываем высоту сугроба на высоту по умолчанию
                if snowdrift_height == N * 10:
                    snowdrift_height = 10
                # Если длина списка упавших снежинок кратна N (т.е. если упала вся порция), увеличиваем шаг
                elif len(fallen_snowflakes) % N == 0:
                    snowdrift_height += 10
                for flake in fallen_snowflakes:
                    center = sd.get_point(flake[0], flake[1])
                    sd.snowflake(center, length=flake[2])
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

    sd.pause()


# функция для отрисовки анимированной радуги, солнца и снега со статичным сугробом
# start_color - базовый внешний цвет радуги. 0 и числа, кратные 7 - красный, числа, кратные 6 - фиолтеовый
# rainbow_delta - задаёт центр радуги относительно оси X, 0 - левый край экрана, 1 - правый
# snowdrift_start - задаёт нижний край сугроба относительно низа экрана. 0 - снизу, 1 - с самого верха

def animated_sky (N=20, start_color=0, rainbow_delta=0.5, snowdrift_start=0):

    from rainbow import rainbow
    import simple_draw as sd
    from sun import sun
    from house import house, field
    from tree import blossom_tree

    sd.set_screen_size(1200, 800)
    # задаём параметры для генерации снежинок
    max_x = sd.resolution[0] - 100
    max_y = sd.resolution[1] + 200
    min_y = sd.resolution[1] + 100
    snowflakes = []

    # генерируем первые снежинки
    for _ in range(N):
        x = sd.random_number(100, max_x)
        y = sd.random_number(min_y, max_y)
        lengh = sd.random_number(10, 25)
        snowflakes.append([x, y, lengh])

    # генерируем сугроб
    snowpile_start = snowdrift_start * sd.resolution[1]
    snowpile = snowdrift(base_height=snowpile_start, max_x=sd.resolution[0])

    # генерируем сугроб слева от дома
    left_snowpile = snowdrift(N=15, base_height=int(sd.resolution[1]*.25), max_x=int(sd.resolution[0]*.4))

    # определяем переменные для анимирования радуги и солнца
    # rainbow_counter определяет задержку смены цветов радуги, чтобы она не мигала, как стробоскоп
    rainbow_counter = 0
    beam_1_lenght = 25
    beams = []
    sun_center = (0, 0)

    # рисуем деревья для фона
    sd.start_drawing()
    first_tree_start_x = int(sd.resolution[0])*.75
    first_tree_start_y = int(sd.resolution[1]*.25)
    first_tree_start = sd.get_point(first_tree_start_x, first_tree_start_y)
    second_tree_start_x = int(sd.resolution[0]*.85)
    second_tree_start_y = first_tree_start_y
    blossom_tree(first_tree_start, 90, 100)
    second_tree_start = sd.get_point(second_tree_start_x, second_tree_start_y)
    blossom_tree(second_tree_start, 90, 75)
    sd.finish_drawing()
    sd.take_background()


    # начинаем отрисовку кадра
    while True:
        sd.start_drawing()
        sd.draw_background()

        # рисуем анимированное солнце
        if len(beams) > 0:
            # стираем положение лучей из предыдущего кадра
            for beam in beams:
                beam[0].draw(color=sd.background_color)
                beam[1].draw(color=sd.background_color)
            sd.circle(center_position=sun_center, color=sd.COLOR_YELLOW, radius=25, width=0)
        # рисуем солнце и получаем данные для стирания этого кадра в новом.
        beams, sun_center = sun(beam_1_lenght)
        beam_1_lenght += 2
        if beam_1_lenght > 55:
            beam_1_lenght = 25

        # рисуем анимированную радугу
        rainbow(start_color, rainbow_delta)
        rainbow_counter += 1
        if rainbow_counter == 5:
            start_color += 1
            if start_color == 7:
                start_color = 0
            rainbow_counter = 0

        # рисуем поле, левый сугроб и дом на среднем плане
        field()
        for flake in left_snowpile:
            flake_center = sd.get_point(flake[0], flake[1])
            sd.snowflake(flake_center, flake[2])
        house()

        # рисуем анимированные снежинки на переднем плане
        for i in range(N):
            snowflake_x = snowflakes[i][0]
            snowflake_y = snowflakes[i][1]
            snowflake_length = snowflakes[i][2]
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length, color=sd.background_color)
            snowflake_x += sd.random_number(-30, 30)
            snowflake_y -= 15
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length)
            snowflakes[i][0] = snowflake_x
            snowflakes[i][1] = snowflake_y
            if snowflake_y <= 0:
                snowflakes[i][1] = sd.random_number(min_y, max_y)

        # рисуем большой сугроб
        for flake in snowpile:
            flake_center = sd.get_point(flake[0], flake [1])
            sd.snowflake(flake_center, flake[2])
        # заканчиваем отрисовку кадра
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
    sd.pause()

animated_sky(rainbow_delta=1, snowdrift_start=0.25)