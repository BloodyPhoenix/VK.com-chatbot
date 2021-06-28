import decimal
import unittest
import os
import dungeon_engine


class TestLocation(unittest.TestCase):

    def setUp(self):
        os.chdir("..")
        self.dungeon = dungeon_engine.load_dungeon()
        self.game = dungeon_engine.Gameplay('123456.0987654321')
        os.chdir("tests")

    def test_location(self):
        location = dungeon_engine.Location(self.dungeon, "Location_0_tm0")
        monster = dungeon_engine.Monster("Mob_exp10_tm0")
        self.assertEqual(location.mobs, [monster])
        self.assertEqual(location.exits, ["Location_1_tm1040", "Location_2_tm33300"])

    def test_gameplay_base_location(self):
        location = dungeon_engine.Location(self.dungeon, "Location_0_tm0")
        self.assertEqual(self.game.location_data, self.dungeon)
        self.assertEqual(self.game.location_name, "Location_0_tm0")
        self.assertEqual(location.mobs, self.game.current_location.mobs)
        self.assertEqual(isinstance(self.game.location_data, dict), True)

    def test_location_change(self):
        location = dungeon_engine.Location(
            self.game.location_data["Location_0_tm0"][1], "Location_1_tm1040"
        )
        self.game._change_location("Location_1_tm1040")
        remaining_time = decimal.Decimal('122416.0987654321')
        time_passed = decimal.Decimal("1040")
        self.game.hero.decrease_time(time_passed)
        self.assertEqual(self.game.current_location, location)
        self.assertEqual(time_passed, self.game.hero.time_passed)
        self.assertEqual(remaining_time, self.game.hero.time_left)

    def test_move_func(self):
        location = dungeon_engine.Location(
            self.game.location_data["Location_0_tm0"][2], "Location_2_tm33300"
        )
        self.game.current_location.exits.remove("Location_1_tm1040")
        self.game._move()
        self.assertEqual(self.game.location_name, "Location_2_tm33300")
        remaining_time = decimal.Decimal('90156.0987654321')
        time_passed = decimal.Decimal("33300")
        self.assertEqual(self.game.current_location, location)
        self.assertEqual(time_passed, self.game.hero.time_passed)
        self.assertEqual(remaining_time, self.game.hero.time_left)


if __name__ == "__main__":
    TestLocation()

