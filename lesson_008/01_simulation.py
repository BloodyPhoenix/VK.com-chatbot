from termcolor import cprint
from random import randint
from random import shuffle


class House:

    def __init__(self, cats_count):
        self.money = 100
        self.food = 50
        self.cat_food = cats_count * 10
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

    def __init__(self, house, cats_count):
        self.fullness = 30
        self.happines = 100
        self.house = house
        self.cats_count = cats_count

    def __str__(self):
        return f"Моя сытость {self.fullness}, мой уровень счастья {self.happines}."

    def check_house_dirt(self):
        if self.house.dirt > 90:
            self.happines -= 10

    def check_if_alive(self):
        if self.fullness <= 0:
            return False
        elif self.happines <= 0:
            return False
        else:
            return True

    def eat(self):
        if 0 < self.house.food <= 30:
            self.fullness += self.house.food
            self.house.food_eaten += self.house.food
            self.house.food = 0
            return True
        elif self.house.food > 30:
            self.fullness += 30
            self.house.food_eaten += 30
            self.house.food -= 30
            return True
        else:
            self.fullness -= 10
            return False

    def buy_cat_food(self):
        self.fullness -= 10
        if self.house.money >= self.cats_count * 30:
            self.house.cat_food += self.cats_count * 30
            self.house.money -= self.cats_count * 30
        else:
            self.house.cat_food = self.house.money
            self.house.money = 0

    def pet_the_cat(self):
        self.happines += 10


class Husband(Human):

    def __init__(self, house, cats_count, salary):
        super().__init__(house=house, cats_count=cats_count)
        self.salary = salary

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.happines <= 20:
            self.play_tanks()
        elif self.house.money <= 250:
            self.work()
        elif self.house.cat_food <= int(self.cats_count) * 10 + 20:
            self.buy_cat_food()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.play_tanks()
        else:
            self.pet_the_cat()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        self.house.total_money_earned += 150

    def play_tanks(self):
        self.happines += 50
        self.fullness -= 10


class Wife(Human):

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.happines <= 20:
            self.buy_jewel()
        elif self.house.food <= 50:
            self.shopping()
        elif self.house.cat_food <= int(self.cats_count) * 10 + 20:
            self.buy_cat_food()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.eat()
        elif dice == 4:
            self.buy_jewel()
        else:
            self.pet_the_cat()

    def shopping(self):
        self.fullness -= 10
        if self.house.money > 60:
            self.house.money -= 60
            self.house.food += 60
        else:
            self.house.food += self.house.money
            self.house.money = 0

    def buy_jewel(self):
        self.fullness -= 10
        if self.house.money >= 400:
            self.happines += 100
            self.house.jewels += 1
            self.house.money -= 350
            # Ювелирку в больших количествах как-то логичнее покупать, чем шубы...
        else:
            self.happines -= 10

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt <= 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100


class Cat:

    def __init__(self, house):
        self.fullness = 30
        self.house = house

    def __str__(self):
        return f"Моя сытость {self.fullness}."

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.soil()
        elif dice <= 3:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.cat_food >= 20:
            self.fullness += 20
            self.house.cat_food -= 20
        elif self.house.cat_food > 0:
            self.fullness += self.house.cat_food
            self.house.cat_food = 0
        else:
            self.fullness -= 10

    def sleep(self):
        self.fullness -= 10

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5

    def check_if_alive(self):
        if self.fullness <= 0:
            return False
        else:
            return True


class Child(Human):

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice <= 3:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if 0 < self.house.food:
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 10

    def sleep(self):
        self.fullness -= 10


class Simulation:

    def __init__(self, food_incidents_count, money_incidents_count):
        self.food_incidents_count = food_incidents_count
        self.money_incidents_count = money_incidents_count

    def create_house_and_residents(self, salary, cats_count):
        self.house = House(cats_count)
        self.residents = []
        self.husband = Husband(house=self.house, salary=salary, cats_count=cats_count)
        self.wife = Wife(house=self.house, cats_count=cats_count)
        self.child = Child(house=self.house, cats_count=0)
        self.residents.append(self.husband)
        self.residents.append(self.wife)
        self.residents.append(self.child)

    def add_cats(self, cats_count):
        cats = []
        for _ in range(cats_count):
            cats.append(Cat(house=self.house))
        self.residents += cats

    def generate_insidents(self):
        self.food_incidents = []
        self.money_incidents = []
        for _ in range (self.food_incidents_count):
            day = randint(1, 365)
            self.food_incidents.append(day)
        for _ in range (self.money_incidents_count):
            day = randint(1, 365)
            self.money_incidents.append(day)

    def year_cycle(self):
        for day in range(1, 366):
            if day in self.food_incidents:
                self.house.food = 0
            if day in self.money_incidents:
                self.house.money = 0
            shuffle(self.residents)
            for resident in self.residents:
                resident.act()
            self.house.add_dirt()
            for resident in self.residents:
                if isinstance(resident, Husband) or isinstance(resident, Wife):
                    resident.check_house_dirt()
            if any([not resident.check_if_alive() for resident in self.residents]):
                return False
        return True

    def experiment(self):
        cats_count = 3
        self.generate_insidents()
        results = []
        while cats_count < 11:
            result = False
            for salary in range (50, 401, 50):
                tests_failed = 0
                for _ in range(3):
                    self.create_house_and_residents(salary=salary, cats_count=cats_count)
                    self.add_cats(cats_count)
                    if not self.year_cycle():
                        tests_failed += 1
                if tests_failed < 2:
                    if not result:
                        result = [cats_count, salary]
                        results.append(result)
            cats_count += 1
        return results

    def result(self):
        results = self.experiment()
        if all(not result for result in results):
            cprint(f"При количестве инцидентов с едой {self.food_incidents_count} и {self.money_incidents_count}"
                   f" с деньгами невозможно прокормить трёх и более котов", color="red")
        else:
            for result in results:
                if result:
                    cprint(f"При количестве инцидентов с едой {self.food_incidents_count} и {self.money_incidents_count}"
                           f" с деньгами можно прокормить {result[0]} котов при минимальной зарплате {result[1]}",
                           color="green")


for money_incidents_counter in range (1, 6):
    for food_incidents_counter in range (1, 6):
        life = Simulation(money_incidents_count=money_incidents_counter, food_incidents_count=food_incidents_counter)
        life.result()
