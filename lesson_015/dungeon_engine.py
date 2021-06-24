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

    def change_location(self, new_location):
        for obj in self.location_data[self.location_name]:
            if isinstance(obj, dict):
                if new_location in obj:
                    self.location_data = obj
                    self.location_name = new_location
                    self.current_location = Location(self.location_data, self.location_name)


def load_dungeon(name="rpg.json"):
    with open(name, "r", encoding="utf-8") as json_map:
        dungeon = json.load(json_map)
        return dungeon
