# -*- coding: utf-8 -*-

def wall(start_x=50, end_x=450, start_y=50, end_y=450, side_x_length=100, side_y_length=50, color_1=(0, 0, 0),
         color_2=(124, 124, 124)):
    import simple_draw as draw

    for row, y in enumerate(range(start_y, end_y, side_y_length)):
        for x in range(start_x, end_x, side_x_length):
            start_point = draw.get_point(x, y)
            final_point = draw.get_point(x + side_x_length, y + side_y_length)
            draw.rectangle(start_point, final_point, color_1, width=0)

    for row, y in enumerate(range(start_y, end_y, side_y_length)):
        if row % 2 == 0:
            zero_point = start_x
        else:
            zero_point = start_x + int(side_x_length * .5)
        for x in range(zero_point, end_x, side_x_length):
            start_point = draw.get_point(x, y)
            final_point = draw.get_point(x + side_x_length, y + side_y_length)
            draw.rectangle(start_point, final_point, color_2, width=1)


def house(window_position=0.8, blink=0):
    import simple_draw as sd
    from lesson_005.drawing import shapes

    # Делаем относительное позиционирование, отсчитывая положение и размер дома исходя из размеров экрана
    # Функция wall даёт смещение на подлины кирпича вправо
    house_sidex_length = int(sd.resolution[0] * .4)
    house_sidey_length = int(sd.resolution[1] * .5)
    house_brick_x = int(house_sidex_length * .2)
    house_brick_y = int(house_sidey_length * .1)
    house_start_x = int(sd.resolution[0] * .5 - sd.resolution[0] * .15) - int(house_brick_x * .5)
    house_fin_x = int(sd.resolution[0] * .5 + sd.resolution[0] * .15)
    house_start_y = int(sd.resolution[1] * .66 - sd.resolution[1] * .5)
    house_fin_y = int((sd.resolution[1] * .5))

    wall(
        start_x=house_start_x,
        end_x=house_fin_x,
        side_x_length=house_brick_x,
        start_y=house_start_y,
        end_y=house_fin_y,
        side_y_length=house_brick_y,
        color_1=sd.COLOR_DARK_ORANGE,
        color_2=(0, 0, 0)
    )

    # рисуем крышу, отталкиваясь от параметров начала/конца дома и не забывая учитывать смещения из-за особенностей
    # работы функции wall
    roof_start = sd.get_point(
        int(house_start_x - sd.resolution[0] * .05),
        int(house_fin_y)
    )
    roof_second = sd.get_point(
        int(house_fin_x + house_brick_x * .5 + sd.resolution[0] * .05),
        int(house_fin_y)
    )
    roof_third = sd.get_point(int(sd.resolution[0] * .5), int(house_fin_y + sd.resolution[1] * .25))
    sd.polygon([roof_start, roof_second, roof_third], sd.COLOR_DARK_GREEN, width=0)

    # рисуем окно
    window_start_y = int(sd.resolution[1] * .3)
    window_start_x = int(house_fin_x - house_sidex_length * window_position)
    window_start = sd.get_point(window_start_x, window_start_y)
    sd.square(left_bottom=window_start, side=house_brick_x, color=sd.COLOR_DARK_CYAN, width=0)

    # пределяем точки для рисования рамы
    second_point = sd.get_point(
        int(house_fin_x - house_sidex_length * window_position + house_brick_x * .5),
        int(sd.resolution[1] * .3)
    )

    third_point = sd.get_point(
        int(house_fin_x - house_sidex_length * window_position),
        int(sd.resolution[1] * .3  + house_brick_x * .5)
    )

    fourth_point = sd.get_point(
        int(house_fin_x - house_sidex_length * window_position + house_brick_x * .5),
        int(sd.resolution[1] * .3 + house_brick_x * .5)
    )

    # рисуем рожицу в окне
    if blink == 0:
        shapes.smile_open_eyes(
            int(house_fin_x - house_sidex_length * window_position + house_brick_x * .5),
            int(sd.resolution[1] * .3) + 30,
            color=(sd.COLOR_YELLOW)
        )

    else:
        shapes.smile_closed_eyes(
            int(house_fin_x - house_sidex_length * window_position + house_brick_x * .5),
            int(sd.resolution[1] * .3) + 30,
            color=(sd.COLOR_YELLOW)
        )


    # рисуем раму
    shapes.draw_square(window_start, int(house_brick_x * .5), color=sd.COLOR_DARK_YELLOW, width=2)
    shapes.draw_square(second_point, int(house_brick_x*.5), color = sd.COLOR_DARK_YELLOW, width=2)
    shapes.draw_square(third_point, int(house_brick_x * .5), color=sd.COLOR_DARK_YELLOW, width=2)
    shapes.draw_square(fourth_point, int(house_brick_x * .5), color=sd.COLOR_DARK_YELLOW, width=2)



def field():
    import simple_draw as sd

    # рисуем поле овалом, чтобы было натуральнее
    field_start = sd.get_point(int(0 - sd.resolution[0] * 0.5), int(0 - sd.resolution[1] * 0.5))
    field_end = sd.get_point(int(sd.resolution[0] + sd.resolution[0] * 0.52), int(sd.resolution[1] * 0.3))
    sd.ellipse(field_start, field_end, color=sd.COLOR_DARK_GREEN)

