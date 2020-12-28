# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0
        self.jewels = 0
        self.food_eaten = 0
        self.total_money_earned = 0

    def __str__(self):
        return f"Денег в доме {self.money}, еды в доме {self.food}, кошачьего корма в доме {self.cat_food}" \
               f", грязи в доме {self.dirt}."

    def add_dirt(self):
        self.dirt += 5

    def year_result(self):
        cprint(f"Денег за год заработано: {self.total_money_earned}", color="yellow")
        cprint(f"Еды съедено: {self.food_eaten}", color="yellow")
        cprint(f"Украшений куплено: {self.jewels}", color="yellow")


class Human:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happines = 100
        self.house = house

    def __str__(self):
        return f"Я {self.name}. Моя сытость {self.fullness}, мой уровень счастья {self.happines}. Живём!"

    def check_house_dirt(self):
        if self.house.dirt > 90:
            self.happines -= 10

    def check_if_alive(self):
        if self.fullness <= 0:
            cprint(f"{self.name} - смерть от голода", color="red")
            return False
        elif self.happines <= 10:
            cprint(f"{self.name} - смерть от депрессии", color="red")
            return False
        else:
            return True

    def eat(self, action):
        if 0 < self.house.food <= 30:
            self.fullness += self.house.food
            self.house.food_eaten += self.house.food
            self.house.food = 0
            return True
        elif self.house.food > 30:
            self.fullness += 30
            self.house.food_eaten += 30
            self.house.food -= 30
            cprint(f"{self.name} {action}.", color="yellow")
            return True
        else:
            self.fullness -= 10
            cprint("В доме нет еды!", color="red")
            return False

    def buy_cat_food(self, action):
        self.fullness -= 10
        if self.house.money >= 30:
            self.house.cat_food += 30
            self.house.money -= 30
            cprint(f"{self.name} {action} кошачий корм")
        else:
            cprint("В доме нет денег на кошачий корм!", color="red")

    def pet_the_cat(self, cat, action):
        self.happines += 5
        cprint(f"{self.name} {action} кота по имени {cat.name}", color="green")


class Husband(Human):
    def act(self, cat):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.happines <= 20:
            self.play_tanks()
        elif self.house.money <= 250:
            self.work()
        elif self.house.cat_food <= 20:
            self.buy_cat_food(action="купил")
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.play_tanks()
        else:
            self.pet_the_cat(cat=cat, action="погладил")

    def eat(self, action="поел"):
        super().eat(action)

    def work(self):
        self.fullness -= 10
        self.happines -= 10
        # TODO даже с зарплатой в 70 у них все нормально
        self.house.money += 150
        self.house.total_money_earned += 150
        cprint(f"{self.name} сходил на работу", color="magenta")

    def play_tanks(self):
        self.happines += 20
        self.fullness -= 10
        cprint(f"{self.name} играл в танки весь день. {self.name} доволен!", color="green")


class Wife(Human):

    def act(self, cat):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.happines <= 20:
            self.buy_jewel()
        elif self.house.food <= 50:
            self.shopping()
        elif self.house.cat_food <= 20:
            self.buy_cat_food(action="купила")
        elif dice <= 2:
            self.clean_house()
        elif dice == 3:
            self.eat()
        elif dice == 4:
            self.buy_jewel()
        else:
            self.pet_the_cat(cat=cat, action="погладила")

    def eat(self, action="поела"):
        super().eat(action)

    def shopping(self):
        self.fullness -= 10
        if self.house.money == 0:
            cprint(f"{self.name} хотела сходить в магазин, но в доме нет денег даже на еду.", color="red")
        elif self.house.money > 60:
            self.house.money -= 60
            self.house.food += 60
            cprint(f"{self.name} сходила в магазин", color="magenta")
        else:
            self.house.food += self.house.money
            self.house.money = 0
            cprint(f"{self.name} сходила в магазин", color="magenta")

    def buy_jewel(self):
        self.fullness -= 10
        if self.house.money >= 400:
            self.happines += 60
            self.house.jewels += 1
            self.house.money -= 350
            # Ювелирку в больших количествах как-то логичнее покупать, чем шубы...
            cprint(f"{self.name} купила ювелирное украшение. {self.name} довольна!", color="green")
        else:
            self.happines -= 10
            cprint(f"{self.name} хотела купить новое украшение, но в доме нет денег!", color="red")

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt <= 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100
        cprint(f"{self.name} убрала дом", color="magenta")

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return f"Я {self.name}. Моя сытость {self.fullness}. Живём!"

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice <= 3:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if self.house.cat_food >= 20:
            self.fullness += 20
            self.house.cat_food -= 20
            cprint(f"{self.name} поел", color="green")
        elif self.house.cat_food > 0:
            self.fullness += self.house.cat_food
            self.house.cat_food = 0
            cprint(f"{self.name} поел", color="green")
        else:
            self.fullness -= 10
            cprint("Безобразие! коту нечего есть!", color="red")

    def sleep(self):
        self.fullness -= 10
        cprint(f"{self.name} спал целый день", color="yellow")

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f"{self.name} драл обои. {self.name} хороший кот.", color="magenta")

    def check_if_alive(self):
        if self.fullness <= 0:
            cprint(f"{self.name} - смерть от голода", color="red")
            return False
        else:
            return True


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice <= 3:
            self.eat()
        else:
            self.sleep()

    def eat(self, action="поел"):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            cprint(f"{self.name} {action}", color="green")
        else:
            cprint("Ребёнку нечего есть!", color="red")

    def sleep(self):
        self.fullness -= 10
        cprint(f"{self.name} спал весь день", color="magenta")


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)
#
for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act(cat=murzik)
    masha.act(cat=murzik)
    kolya.act()
    murzik.act()
    home.add_dirt()
    serge.check_house_dirt()
    masha.check_house_dirt()
    print('--- в конце дня ---')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color="cyan")
    cprint(murzik, color="cyan")
    cprint(home, color='cyan')
    # TODO для переноса строки страраемся не использовать символ \
    # TODO поробуйте создать с список из жильцов и использовать функцию any()
    if not serge.check_if_alive() or not masha.check_if_alive() or not kolya.check_if_alive() or \
        not murzik.check_if_alive():
        break
home.year_result()

# TODO из 15 запусков не разу не было фейла, они живут 100% такого быть не должно
# TODO Нужно добиться результата 70 на 30 или 80 на 20%
# TODO Есть вероятность что показатели или логика сильно притянута.

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
