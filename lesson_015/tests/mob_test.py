import decimal
import unittest
import os
from lesson_015 import dungeon_engine


class TestMob(unittest.TestCase):

    def setUp(self):
        os.chdir("..")
        self.dungeon = dungeon_engine.load_dungeon()
        self.game = dungeon_engine.Gameplay('123456.0987654321')
        os.chdir("tests")
        self.game.current_location.mobs = ["Mob_exp30_tm30"]

    def test_mob(self):
        exp = decimal.Decimal("30")
        remaining_time = decimal.Decimal('123426.0987654321')
        time_passed = decimal.Decimal("30")
        self.game._fight()
        self.assertEqual(self.game.exp, exp)
        self.assertEqual(remaining_time, self.game.remaining_time)
        self.assertEqual(time_passed, self.game.time_passed)
        self.assertEqual(0, len(self.game.current_location.mobs))


if __name__ == "__main__":
    TestMob()
