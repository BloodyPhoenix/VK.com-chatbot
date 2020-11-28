# -*- coding: utf-8 -*-


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint, shuffle

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, моя сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 10
            cprint(f'{self.name} нет еды', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint(f'{self.name} смотрел MTV целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за едой', color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} вьехал в дом', color='cyan')

    def take_cat(self, cat):
        if self.house:
            cat.house = self.house
            cprint(f"Завёл кота по имени {cat.name}", color="green")
        else:
            cprint(f"У человека по имени {self.name} нет дома!", color="red")

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint(f'{self.name} купил кошачий корм', color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def clean_house(self):
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.fullness -= 20
        cprint(f"{self.name} убрал дом", color="magenta")

    def act(self):
        dice = randint(1, 6)
        if self.house.money < 50:
            self.work()
        elif self.house.cat_food <= 10:
            self.buy_cat_food()
        elif self.house.food < 10:
            self.shopping()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def check_if_alive(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return False
        return True


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return f"Я - {self.name}, моя сытость {self.fullness}"

    def tear_wallpaper(self):
        self.house.dirt += 5
        self.fullness -= 10
        cprint(f"{self.name} драл обои. {self.name} хороший кот", color="yellow")

    def eat(self):
        #  Я его так усложнила, когда тестила 2 и более котов, чтобы кот хотя бы один день прожил, если еды нет
        # А потом, когда она появилась - отъелся до максимальной сытости.
        # Кстати, не имеет ли смысл сделать смерть, если сытость строго меньше 0, а не меньше или равна?
        # Чтобы был запас времени на поесть
        # TODO вообще не принципиально, потому что мы кормим котов >=10
        # TODO принципиально, когда в какой-то день одному коту еды хватило, а второму - уже нет.

        if self.house.cat_food >= 10:
            if self.fullness % 10 == 0:
                self.fullness += 20
                self.house.cat_food -= 10
            elif self.house.cat_food == 5:
                self.fullness += 10
                self.house.cat_food -= 5
            else:
                self.fullness += 25
                self.house.cat_food -= 15
            cprint(f"{self.name} поел", color="green")
        else:
            cprint(f"Безобразие! Коту нечего есть!", color="red")
            self.fullness -= 5

    def sleep(self):
        self.fullness -= 10
        cprint(f"{self.name} спал весь день", color="green")

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice <= 3:
            self.tear_wallpaper()
        else:
            self.sleep()

    def check_if_alive(self):
        if self.fullness <= 0:
            cprint(f"{self.name} умер...", color="red")
            return False
        else:
            return True


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме еды осталось {self.food}, кошачьего корма осталось {self.cat_food}, ' \
               f'денег осталось {self.money}, грязи в доме - {self.dirt}'


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

my_home = House()
human_slave = Man("Человеческий раб")
cats = [Cat("Царь"), Cat("Император"), Cat("Король")]
human_slave.go_to_the_house(my_home)

# TODO думаю этого делать не стоит, пусть сам в действиях о себе позаботится !
# TODO Пробовала. Или не прописывать уменьшение сытости от заведения котов, или кормить вручную до начала цикла.
# TODO Иначе смерть на 3-4 день из-за того, что он не успевает кормить себя, котов, покупать корм и т.д.
# TODO Или надо дать возможность ему пожить денёк при уровне сытости, равном нолю.

# Тут надо до начала основного цикла принудительно покормить человека или не прописывать ему уменьшение сытости от
# того, что он завёл котов. Иначе он сразу умирает...
for cat in cats:
    human_slave.take_cat(cat)



# Если повезёт, человек может прокормить трёх котов. Если не повезёт - человек умрёт от голода, не успевая кормить котов
# и убирать за ними. Или умрёт кот...


for day in range(1, 366):
    print(f'================ день {day} ==================')
    human_slave.act()
    shuffle(cats)
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for cat in cats:
        print(cat)
    print(human_slave)
    print(my_home)
    if not human_slave.check_if_alive():
        break
    for cat in cats:
        if not cat.check_if_alive():
            del cat
    if not cats:
        cprint("Все коты умерли!", color="red")
        break

