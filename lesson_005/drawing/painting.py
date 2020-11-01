# -*- coding: utf-8 -*-

def static_painting ():

    # TODO импорты делаются в самом начале модуля!
    import simple_draw as draw
    from drawing import rainbow, snow, sun, tree, house

    draw.set_screen_size(1200, 600)

    draw.start_drawing()
    sun.sun()
    rainbow.rainbow(rainbow_delta=1)

    house.field()
    snowpile = snow.snowdrift(N=15, base_height=int(draw.resolution[1]*0.25), max_x=int(draw.resolution[0]*0.3))
    for flake in snowpile:
        flake_center = draw.get_point(flake[0], flake[1])
        draw.snowflake(flake_center, flake[2])
    house.house()

    first_tree_x = int(draw.resolution[0] * .75)
    first_tree_y = int(draw.resolution[1] * .25)
    first_tree_start = draw.get_point(first_tree_x, first_tree_y)
    tree.blossom_tree(first_tree_start, 90, 75)
    second_tree_x = int(draw.resolution[0] * .95)
    second_tree_y = int(draw.resolution[1] * .2)
    second_tree_start = draw.get_point(second_tree_x, second_tree_y)
    tree.blossom_tree(second_tree_start, 90, 100)
    third_tree_x = int(draw.resolution[0] * .85)
    third_tree_y = int(draw.resolution[1] * .15)
    third_tree_start = draw.get_point(third_tree_x, third_tree_y)
    tree.blossom_tree(third_tree_start, 90, 65)

    draw.finish_drawing()
    draw.pause()


def animated_painting(resolution = [1200, 800], N=20, start_color=0, rainbow_delta=0.5, snowdrift_start=0):
    import simple_draw as sd
    from drawing import house, rainbow, snow, sun, tree

    if resolution[0] < 800:
        resolution[0] = 800
    if resolution[1] < 600:
        resolution[1] = 600
    sd.set_screen_size(resolution[0], resolution[1])

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
    snowpile = snow.snowdrift(base_height=snowpile_start, max_x=sd.resolution[0])

    # генерируем сугроб слева от дома
    left_snowpile = snow.snowdrift(N=15, base_height=int(sd.resolution[1] * .25), max_x=int(sd.resolution[0] * .4))

    # определяем переменные для анимирования рожицы, радуги и солнца
    # rainbow_counter определяет задержку смены цветов радуги, чтобы она не мигала, как стробоскоп
    blink_counter = 0
    rainbow_counter = 0
    beam_1_lenght = 25
    beams = []
    sun_center = (0, 0)

    # рисуем деревья для фона
    sd.start_drawing()
    first_tree_start_x = int(sd.resolution[0]) * .75
    first_tree_start_y = int(sd.resolution[1] * .25)
    first_tree_start = sd.get_point(first_tree_start_x, first_tree_start_y)
    second_tree_start_x = int(sd.resolution[0] * .85)
    second_tree_start_y = first_tree_start_y
    tree.blossom_tree(first_tree_start, 90, 100)
    second_tree_start = sd.get_point(second_tree_start_x, second_tree_start_y)
    tree.blossom_tree(second_tree_start, 90, 75)
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
        beams, sun_center = sun.sun(beam_1_lenght)
        beam_1_lenght += 2
        if beam_1_lenght > 55:
            beam_1_lenght = 25

        # рисуем анимированную радугу
        rainbow.rainbow(start_color, rainbow_delta)
        rainbow_counter += 1
        if rainbow_counter == 5:
            start_color += 1
            if start_color == 7:
                start_color = 0
            rainbow_counter = 0

        # рисуем поле, левый сугроб и дом на среднем плане
        house.field()
        for flake in left_snowpile:
            flake_center = sd.get_point(flake[0], flake[1])
            sd.snowflake(flake_center, flake[2])

        if blink_counter < 4:
            house.house(blink=0)
        elif blink_counter < 6:
            house.house(blink = 1)
        else:
            house.house(blink=1)
            blink_counter = 0
        blink_counter += 1

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
            flake_center = sd.get_point(flake[0], flake[1])
            sd.snowflake(flake_center, flake[2])
        # заканчиваем отрисовку кадра
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
    sd.pause()

# animated_painting()
# static_painting()
