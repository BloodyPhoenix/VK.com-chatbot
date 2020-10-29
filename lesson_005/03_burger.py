# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger


def double_cheesburger():
    # TODO тут мы не создаем, новый список, нужно вызывать только те функции в нужной последовательности из
    # TODO модуля my_burger
    recipie = ["Состав:"]
    recipie.append(my_burger.add_bread())
    recipie.append(my_burger.add_cutlet())
    recipie.append(my_burger.add_cheese())
    recipie.append(my_burger.add_cutlet())
    recipie.append(my_burger.add_cheese())
    recipie.append(my_burger.add_cucumber())
    recipie.append(my_burger.add_cetchup())
    recipie.append(my_burger.add_bread())
    formated_recipie = "\n"
    formated_recipie = formated_recipie.join(recipie)
    print (formated_recipie)


def my_favorite_burger():
    # TODO аналогично
    recipie = ["Состав:"]
    recipie.append(my_burger.add_bread())
    recipie.append(my_burger.add_cutlet())
    recipie.append(my_burger.add_cheese())
    recipie.append(my_burger.add_tomato())
    recipie.append(my_burger.add_bread())
    formated_recipie = "\n"
    formated_recipie = formated_recipie.join(recipie)
    print(formated_recipie)


my_favorite_burger()


