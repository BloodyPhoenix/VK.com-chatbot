import unittest
import os
from lesson_015 import dungeon_engine


class TestLocation(unittest.TestCase):

    def setUp(self):
        os.chdir("..")
        self.dungeon = dungeon_engine.load_dungeon()
        self.game = dungeon_engine.Gameplay()
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
        self.game.change_location("Location_1_tm1040")
        self.assertEqual(self.game.location_name, "Location_1_tm1040")
        location_data = None
        for obj in self.dungeon["Location_0_tm0"]:
            if isinstance(obj, dict):
                if "Location_1_tm1040" in obj:
                    location_data = obj
        self.assertEqual(self.game.location_data, location_data)
        self.assertEqual(location.mobs, self.game.current_location.mobs)
        self.assertEqual(location.exits, self.game.current_location.exits)


if __name__ == "__main__":
    TestLocation()

