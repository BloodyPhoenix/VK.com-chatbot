# -*- coding: utf-8 -*-

def wall(start_x=50, end_x=450, start_y=50, end_y=450, side_x_length=100, side_y_length=50, color_1 = (0, 0, 0),
         color_2 = (124, 124, 124)):

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
            zero_point = start_x+int(side_x_length*.5)
        for x in range(zero_point, end_x, side_x_length):
            start_point = draw.get_point(x, y)
            final_point = draw.get_point(x + side_x_length, y + side_y_length)
            draw.rectangle(start_point, final_point, color_2, width=1)

def house():

    import simple_draw as sd

    #Делаем относительное позиционирования, отсчитывая положение и размер дома исходя из размеров экрана
    house_side_lenth = int(sd.resolution[0] * .4)
    house_brick_x = int(house_side_lenth * .2)
    house_brick_y = int(house_side_lenth * .1)
    house_start_x = int(sd.resolution[0] * .5 - sd.resolution[0] * .15) - int(house_brick_x * .5)
    house_fin_x = int(sd.resolution[0] * .5 + sd.resolution[0] * .15)
    house_start_y = int(sd.resolution[1] * .66 - sd.resolution[1] * .5)
    house_fin_y = int((sd.resolution[1] * .66) - house_brick_x)


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

    roof_start = sd.get_point(int(house_start_x - sd.resolution[0] * .05), house_fin_y)
    roof_second = sd.get_point(int(house_fin_x + house_brick_x*.5 + sd.resolution[0] * .05), house_fin_y)
    roof_third = sd.get_point(int(sd.resolution[0]*.5), int (house_fin_y + sd.resolution[1] * .25))
    sd.polygon([roof_start, roof_second, roof_third], sd.COLOR_DARK_GREEN, width=0)


def field():

     import simple_draw as sd

     field_start = sd.get_point(int(0 - sd.resolution[0] * 0.5), int(0 - sd.resolution[1] * 0.5))
     field_end = sd.get_point(int(sd.resolution[0] + sd.resolution[0] * 0.52), int(sd.resolution[1] * 0.3))
     sd.ellipse(field_start, field_end, color=sd.COLOR_DARK_GREEN)



