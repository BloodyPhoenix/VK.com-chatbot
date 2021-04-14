# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageFont, ImageColor
import os
import argparse


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


def make_ticket(fio, from_, to, date, path=None):
    ticket = os.path.normpath("images/ticket_template.png")
    ticket = Image.open(ticket)
    font = ImageFont.truetype("ofont.ru_Romul.ttf", size=14)
    draw = ImageDraw.Draw(ticket)
    draw.text((45, 130), text=fio, font=font, fill=ImageColor.colormap["black"])
    draw.text((45, 200), text=from_, font=font, fill=ImageColor.colormap["black"])
    draw.text((45, 265), text=to, font=font, fill=ImageColor.colormap["black"])
    draw.text((280, 265), text=str(date), font=font, fill=ImageColor.colormap["black"])
    filename = "ticket for "+str(fio)+".png"
    if path:
        save_path = os.path.join(path, filename)
    else:
        save_path = os.path.join("images", filename)
    ticket.save(save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A ticket maker")
    parser.add_argument("ticket_name", default=None, type=str, help="Name of a ticket owner")
    parser.add_argument("ticket_from", default=None, type=str, help="Departure point")
    parser.add_argument("ticket_to", default=None, type=str, help="Destination")
    parser.add_argument("ticket_date", default=None, type=str, help="A date of departure")
    parser.add_argument("-s", "--save_to", default=None, type=str, help="A directory for a new ticket")
    args = parser.parse_args()
    fio = args.ticket_name
    from_ = args.ticket_from
    to = args.ticket_to
    date = args.ticket_date
    path = args.save_to
    make_ticket(fio=fio, from_=from_, to=to, date=date, path=path)

