# -*- coding: utf-8 -*-

def snowdrift(N=20):

    import simple_draw as sd

    min_x = 0
    max_x = sd.resolution[0]
    start_y = sd.resolution[1]+200
    snowflakes = []
    fallen_snowflakes = []
    snowdrift_height = 0

    for _ in range(N):
        x = sd.random_number(min_x, max_x)
        y = start_y
        lengh = sd.random_number(10, 100)
        snowflakes.append([x, y, lengh])

    while len(fallen_snowflakes) <= N*10:
        sd.start_drawing()
        for i in range(N):
            snowflake_x = snowflakes[i][0]
            snowflake_y = snowflakes[i][1]
            snowflake_length = snowflakes[i][2]
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length, color=sd.background_color)
            snowflake_x += sd.random_number(-10, 10)
            snowflake_y -= 10
            center = sd.get_point(snowflake_x, snowflake_y)
            sd.snowflake(center=center, length=snowflake_length)
            snowflakes[i][0] = snowflake_x
            snowflakes[i][1] = snowflake_y
            if snowflake_y <= snowdrift_height:
                fallen_snowflakes.append((snowflake_x, snowflake_y, snowflake_length))
                if snowdrift_height == N*10:
                    snowdrift_height = 10
                elif len(fallen_snowflakes) % N == 0:
                    snowdrift_height += 10
                for flake in fallen_snowflakes:
                    center = sd.get_point(flake[0], flake[1])
                    sd.snowflake(center, length=flake[2])
                min_x += 1
                max_x -= 1
                snowflakes[i][0] = sd.random_number(min_x, max_x)
                snowflakes[i][1] = start_y
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
             break
    sd.pause()

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

def rainbow_snowfall (N=20, start_color=0):

    import rainbow
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
    start_color = start_color
    rainbow_counter = 0

    while True:
        sd.start_drawing()
        rainbow (start_color)
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
        rainbow_counter += 1
        if rainbow_counter == 10:
            start_color += 1
            if start_color == 7:
                start_color = 0
            rainbow_counter = 0
        if sd.user_want_exit():
            break

    sd.pause()

rainbow_snowfall()