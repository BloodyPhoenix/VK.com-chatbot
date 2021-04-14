# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageFont, ImageColor
import os


def make_ticket(fio, from_, to, date):
    ticket = os.path.normpath("images/ticket_template.png")
    ticket = Image.open(ticket)
    font = ImageFont.truetype("ofont.ru_Romul.ttf", size=14)
    draw = ImageDraw.Draw(ticket)
    draw.text((45, 130), text=fio, font=font, fill=ImageColor.colormap["black"])
    draw.text((45, 200), text=from_, font=font, fill=ImageColor.colormap["black"])
    draw.text((45, 265), text=to, font=font, fill=ImageColor.colormap["black"])
    draw.text((280, 265), text=str(date), font=font, fill=ImageColor.colormap["black"])
    # TODO пробелы в имени не желательно писать
    filename = "ticket for "+str(fio)+".png"
    save_path = os.path.join("images", filename)
    ticket.save(save_path)


make_ticket("Ыыы", "Марс", "Плутон", "22.05.2035")

# TODO Делайте вторую часть
# TODO укажите полное ФИО

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

# TODO добавить файл requirements в корень этого модуля.
