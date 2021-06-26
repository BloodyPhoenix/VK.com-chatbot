import decimal
import unittest
import os
from lesson_015 import dungeon_engine


class TestLocation(unittest.TestCase):

    def setUp(self):
        os.chdir("..")
        self.dungeon = dungeon_engine.load_dungeon()
        self.game = dungeon_engine.Gameplay('123456.0987654321')
        os.chdir("tests")

    def test_start_location(self):
        location = dungeon_engine.Location(self.dungeon, "Location_0_tm0")
        self.assertEqual(location.mobs, ["Mob_exp10_tm0"])
        self.assertEqual(location.exits, ["Location_1_tm1040", "Location_2_tm33300"])

    def test_gameplay_base_location(self):
        location = dungeon_engine.Location(self.dungeon, "Location_0_tm0")
        self.assertEqual(self.game.location_data, self.dungeon)
        self.assertEqual(self.game.current_location.mobs, location.mobs)
        self.assertEqual(self.game.current_location.exits, location.exits)
        self.assertEqual(isinstance(self.game.location_data, dict), True)

    def test_location_change(self):
        location = dungeon_engine.Location(
            self.game.location_data["Location_0_tm0"][1], "Location_1_tm1040"
        )
        self.game._change_location("Location_1_tm1040")
        self.assertEqual(self.game.location_name, "Location_1_tm1040")
        location_data = None
        remaining_time = decimal.Decimal('122416.0987654321')
        time_passed = decimal.Decimal("1040")
        self.game._check_time(time_passed)
        for obj in self.dungeon["Location_0_tm0"]:
            if isinstance(obj, dict):
                if "Location_1_tm1040" in obj:
                    location_data = obj
        self.assertEqual(self.game.location_data, location_data)
        self.assertEqual(location.mobs, self.game.current_location.mobs)
        self.assertEqual(location.exits, self.game.current_location.exits)
        self.assertEqual(time_passed, self.game.time_passed)
        self.assertEqual(remaining_time, self.game.remaining_time)

    def test_move_func(self):
        location = dungeon_engine.Location(
            self.game.location_data["Location_0_tm0"][2], "Location_2_tm33300"
        )
        self.game.current_location.exits.remove("Location_1_tm1040")
        self.game._move()
        self.assertEqual(self.game.location_name, "Location_2_tm33300")
        location_data = None
        remaining_time = decimal.Decimal('90156.0987654321')
        time_passed = decimal.Decimal("33300")
        for obj in self.dungeon["Location_0_tm0"]:
            if isinstance(obj, dict):
                if "Location_2_tm33300" in obj:
                    location_data = obj
        self.assertEqual(self.game.location_data, location_data)
        self.assertEqual(location.mobs, self.game.current_location.mobs)
        self.assertEqual(location.exits, self.game.current_location.exits)
        self.assertEqual(time_passed, self.game.time_passed)
        self.assertEqual(remaining_time, self.game.remaining_time)


if __name__ == "__main__":
    TestLocation()

