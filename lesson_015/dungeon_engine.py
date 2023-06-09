import json
import decimal
import re
import datetime
import csv
import os


remaining_time = '123456.0987654321'
field_names = ['current_location', 'current_experience', 'current_date']


class Monster:

    def __init__(self, description: str):
        mob_params = description.split("_")
        self.exp = int(mob_params[1][3:])
        self.time = decimal.Decimal(mob_params[2][2:])

    def __str__(self):
        return f"Монстр exp_{self.exp} time{self.time}"

    def __eq__(self, other):
        if isinstance(other, Monster):
            if self.exp == other.exp and self.time == other.time:
                return True
        return False


class Character:

    def __init__(self, start_time):
        self.time_left = decimal.Decimal(start_time)
        self.time_passed = 0
        self.exp = 0
        self.alive = True

    def decrease_time(self, action_time: decimal.Decimal):
        self.time_left -= action_time
        self.time_passed += action_time
        if self.time_left <= 0:
            self.alive = False

    def fight(self, mob: Monster):
        self.exp += mob.exp
        self.decrease_time(mob.time)


class Location:

    def __init__(self, location_data: dict, location_name: str):
        self.mobs = []
        self.exits = []
        for obj in location_data[location_name]:
            if isinstance(obj, str):
                mob = Monster(obj)
                self.mobs.append(mob)
            elif isinstance(obj, dict):
                for key in obj:
                    self.exits.append(key)

    def __eq__(self, other):
        if isinstance(other, Location):
            if self.mobs == other.mobs and self.exits == other.exits:
                return True
        return False

    def print_description(self):
        print("Внутри вы видите:")
        for mob in self.mobs:
            print(f"Монстра exp_{mob.exp} time_{mob.time}")
        for location_exit in self.exits:
            print(f"Вход в локацию {location_exit}")


class Gameplay:

    def __init__(self, time):
        self.hero = Character(time)
        self.location_name = "Location_0_tm0"
        self.location_data = load_dungeon("rpg.json")
        self.current_location = Location(self.location_data, self.location_name)
        if os.path.exists("dungeon.csv"):
            self.game_data = []
        else:
            self.game_data = [['current_location', 'current_experience', 'current_date']]

    def _change_location(self, new_location):
        for obj in self.location_data[self.location_name]:
            if isinstance(obj, dict):
                if new_location in obj:
                    self.location_data = obj
                    self.location_name = new_location
                    self.current_location = Location(self.location_data, self.location_name)
                    if 0 == len(self.current_location.exits):
                        print("Вы упёрлись в тупик! Игра окончена!")
                        self._game_over()
                    return

    def run(self):
        while True:
            self._add_game_data()
            self._check_time()
            self._choose_action()

    def _add_game_data(self):
        current_location = self.location_name
        current_experience = self.hero.exp
        current_date = datetime.datetime.now().strftime("%H:%m %d.%m.%Y")
        self.game_data.append([current_location, current_experience, current_date])
        return

    def _choose_action(self):
        print(f"Прошло времени: {self.hero.time_passed}")
        print(f"Времени осталось: {self.hero.time_left}")
        print(f"Ваш опыт: {self.hero.exp}")
        print()
        print(f"Вы находитесь в локации {self.location_name}")
        self.current_location.print_description()
        if len(self.current_location.mobs) > 0:
            self._room_with_mobs_action()
            return
        else:
            self._room_without_mobs_action()
            return

    def _check_time(self):
        if not self.hero.alive:
            print("""О нет, наводнение!
Пещеру затопило, и вы потеряли сознание.
Но почему-то вы вновь очнулись перед её входом.
Да что ж это за место такое?!
            
Попробуете ещё раз?""")
            self._game_over()
        else:
            return

    def _room_with_mobs_action(self):
        while True:
            print()
            print("""Выберите действие:
1: Атаковать монстра
2: Перейти в другую локацию
3: Сдаться и выйти из игры""")
            print()
            player_choice = input()
            if len(player_choice) > 1:
                print("Команда не распознана. Повторите ввод")
                continue
            if not re.match(r"[1-3]", player_choice):
                print("Команда не распознана. Повторите ввод")
                continue
            break
        if "1" == player_choice:
            self._fight()
            return
        elif "2" == player_choice:
            self._move()
            return
        else:
            self._exit()

    def _room_without_mobs_action(self):
        while True:
            print()
            print("""Выберите действие:
2: Перейти в другую локацию
3: Сдаться и выйти из игры""")
            print()
            player_choice = input()
            if len(player_choice) > 1:
                print("Команда не распознана. Повторите ввод")
                continue
            if not re.match(r"[2-3]", player_choice):
                print("Команда не распознана. Повторите ввод")
                continue
            break
        if "2" == player_choice:
            self._move()
            return
        else:
            self._exit()

    def _exit(self):
        print()
        print("""Вы уверены, что хотите выйти?
1: начать заново
2: закончить игру
0: продолжить игру""")
        while True:
            print()
            player_choice = input()
            if len(player_choice) > 1:
                print("Команда не распознана. Повторите ввод")
                continue
            if not re.match(r"[0-2]", player_choice):
                print("Команда не распознана. Повторите ввод")
                continue
            break
        if "1" == player_choice:
            self._save_game_data()
            start_game()
        elif "2" == player_choice:
            self._save_game_data()
            exit()
        elif "0" == player_choice:
            self._choose_action()

    def _game_over(self):
        self._save_game_data()
        print(f"На момент окончания игры у вас осталось {self.hero.time_left:.10f} времени.")
        print(f"Вы заработали {self.hero.exp} опыта.")
        print()
        print("""1: начать заново
2: закончить игру""")
        while True:
            print()
            player_choice = input()
            if len(player_choice) > 1:
                print("Команда не распознана. Повторите ввод")
                continue
            if not re.match(r"[1-2]", player_choice):
                print("Команда не распознана. Повторите ввод")
                continue
            break
        if "1" == player_choice:
            start_game()
        elif "2" == player_choice:
            exit()

    def _save_game_data(self):
        with open("dungeon.csv", "a", newline="") as save_file:
            writer = csv.writer(save_file, delimiter=',')
            for line in self.game_data:
                writer.writerow(line)
        return

    def _fight(self):
        options = len(self.current_location.mobs)
        player_choice = 1
        if options > 1:
            print()
            print("Выберите, какого монстра атаковать:")
            for index, mob in enumerate(self.current_location.mobs):
                print(index + 1, mob)
            while True:
                print()
                player_choice = input()
                if player_choice.isdigit():
                    player_choice = int(player_choice)
                    if 0 < player_choice <= options:
                        break
                else:
                    print("Команда не распознана. Повторите ввод")
        print()
        mob_index = player_choice-1
        chosen_mob = self.current_location.mobs[mob_index]
        self.hero.fight(chosen_mob)
        self.current_location.mobs.remove(chosen_mob)
        return

    def _move(self):
        options = len(self.current_location.exits)
        player_choice = 1
        if options > 1:
            print()
            print("Выберите, в какую локацию перейти:")
            for index, mob in enumerate(self.current_location.exits):
                print(index + 1, mob)
            while True:
                print()
                player_choice = input()
                if player_choice.isdigit():
                    player_choice = int(player_choice)
                    if 0 < player_choice <= options:
                        break
                else:
                    print("Команда не распознана. Повторите ввод")
        print()
        exit_index = player_choice - 1
        chosen_exit = self.current_location.exits[exit_index]
        if "Hatch" in chosen_exit:
            action_time = decimal.Decimal("159.098765432")
            if action_time <= self.hero.time_left:
                if self.hero.exp >= 280:
                    self.hero.decrease_time(action_time)
                    print("""Поздравляем! Вы нашли выход!
Сыграть ещё раз?
""")
                    self._game_over()
                else:
                    if 0 == len(self.current_location.mobs):
                        print("""О, нет! У вас недостаточно опыта, чтобы открыть люк!""")
                        self._game_over()
                    else:
                        print("У вас недостаточно опыта, чтобы открыть люк, но в подземелье ещё есть монстры!")
                        return
            else:
                print("""О, нет! Вам не хватило времени, чтобы выбраться наружу!
Вас затопило!
Хотите попробовать ещё раз?""")
                self._game_over()
        location_time = decimal.Decimal(chosen_exit.split("_")[2][2:])
        self.hero.decrease_time(location_time)
        self._change_location(chosen_exit)
        return


def load_dungeon(name="rpg.json"):
    with open(name, "r", encoding="utf-8") as json_map:
        dungeon = json.load(json_map)
        return dungeon


def start_game():
    game = Gameplay(time=remaining_time)
    game.run()
