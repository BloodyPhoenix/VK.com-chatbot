# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# Пусть генерируются до верха экрана
max_x = sd.resolution[0]-100
max_y = sd.resolution[1]+200
min_y = sd.resolution[1]+100
snowflakes = []

for _ in range(N):
    # удалил вам лишние скобки они не нужны
    x = sd.random_number(100, max_x)
    y = sd.random_number(min_y, max_y)
    lengh = sd.random_number(10, 100)
    snowflakes.append([x, y, lengh])

fallen_snowflakes = []

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
            if snowdrift_height == N*10:
                snowdrift_height = 10
            # Если длина списка упавших снежинок кратна N (т.е. если упала вся порция), увеличиваем шаг
            elif len(fallen_snowflakes) % N == 0:
                snowdrift_height += 10
            for flake in fallen_snowflakes:
                center = sd.get_point(flake[0], flake[1])
                sd.snowflake(center, length=flake[2])
            #Создаём новую снежинку, переназначая координату y для упавшей, которая "ушла" в fallen_snowflakes
            snowflakes[i][1] = sd.random_number(min_y, max_y)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
