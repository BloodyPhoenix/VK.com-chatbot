import json
import re


remaining_time = '123456.0987654321'
field_names = ['current_location', 'current_experience', 'current_date']


class Location:

    def __init__(self, location_data: dict, location_name: str):
        self.mobs = []
        self.exits = []
        for obj in location_data[location_name]:
            if isinstance(obj, str):
                self.mobs.append(obj)
            elif isinstance(obj, dict):
                for key in obj:
                    self.exits.append(key)

    def print_description(self):
        print("Внутри вы видите:")
        for mob in self.mobs:
            print(f"Монста {mob}")
        for location_exit in self.exits:
            print(f"Вход в локацию {location_exit}")


class Gameplay:

    def __init__(self):
        self.remaining_time = remaining_time
        self.time_passed = 0
        self.location_name = "Location_0_tm0"
        self.location_data = load_dungeon("rpg.json")
        self.current_location = Location(self.location_data, self.location_name)

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
                    self.choose_action()

    def choose_action(self):
        print(f"Вы находитесь в локации {self.location_name}")
        self.current_location.print_description()
        while True:
            print()
            # TODO Уменьшить количество действий, если в локации нет монстров
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
        elif "2" == player_choice:
            self._move()
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
            start_game()
        elif "2" == player_choice:
            exit()
        elif "0" == player_choice:
            self.choose_action()

    @staticmethod
    def _game_over():
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

        # TODO тратим время, получаем экспу
        print()
        mob_index = player_choice -1
        chosen_mob = self.current_location.mobs[mob_index]
        self.current_location.mobs.remove(chosen_mob)
        self.choose_action()

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

        # TODO Тратим время, переходим в другую локацию
        print()
        exit_index = player_choice - 1
        chosen_exit = self.current_location.exits[exit_index]
        self._change_location(chosen_exit)


def load_dungeon(name="rpg.json"):
    with open(name, "r", encoding="utf-8") as json_map:
        dungeon = json.load(json_map)
        return dungeon


def start_game():
    game = Gameplay()
    game.choose_action()
