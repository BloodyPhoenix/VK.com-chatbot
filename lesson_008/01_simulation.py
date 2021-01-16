from termcolor import cprint
from random import randint
from random import shuffle


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 10
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
        self.happiness = 100
        self.house = house
        self.cats_count = cats_count

    def __str__(self):
        return f"Моя сытость {self.fullness}, мой уровень счастья {self.happiness}."

    def check_house_dirt(self):
        if self.house.dirt > 90:
            self.happiness -= 10

    def check_if_alive(self):
        if self.fullness <= 0:
            return False
        elif self.happiness <= 0:
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
        self.happiness += 10


class Husband(Human):

    def __init__(self, house, cats_count, salary):
        super().__init__(house=house, cats_count=cats_count)
        self.salary = salary

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.happiness <= 20:
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
        self.happiness += 50
        self.fullness -= 10


class Wife(Human):

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.happiness <= 20:
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
            self.happiness += 100
            self.house.jewels += 1
            self.house.money -= 350
            # Ювелирку в больших количествах как-то логичнее покупать, чем шубы...
        else:
            self.happiness -= 10

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
        self.residents = []
        self.food_incidents = []
        self.money_incidents = []
        self.house = House()

    def create_house_and_residents(self, current_salary, cats_count):
        self.house = House()
        self.residents = [
            Husband(house=self.house, salary=current_salary, cats_count=cats_count),
            Wife(house=self.house, cats_count=cats_count),
            Child(house=self.house, cats_count=0)
        ]
        self.money_incidents = []
        self.food_incidents = []
        self.generate_incidents()

    def add_cats(self, cats_count):
        # TODO сделать его параметром класса
        # TODO зачем, если потом этот список вливается в список residents?
        cats = []
        for _ in range(cats_count):
            # TODO тут можно сформировать имя котам используя цикл чтобы
            # TODO можно, но зачем?
            cats.append(Cat(house=self.house))
        self.residents += cats
        self.house.cat_food = cats_count * 10

    def generate_incidents(self):
        for _ in range(self.food_incidents_count):
            day = randint(1, 365)
            self.food_incidents.append(day)
        for _ in range(self.money_incidents_count):
            day = randint(1, 365)
            self.money_incidents.append(day)

    def year_cycle(self, salary, cats_count):
        self.create_house_and_residents(current_salary=salary, cats_count=cats_count)
        self.add_cats(cats_count)
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

    def experiment(self, salary):
        for cats_count in range(10, 0, -1):
            tests_passed = 0
            for _ in range(3):
                if self.year_cycle(salary, cats_count):
                    tests_passed += 1
            if tests_passed == 2:
                return cats_count
        return False


for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            max_cats = life.experiment(salary)
            if max_cats:
                print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
