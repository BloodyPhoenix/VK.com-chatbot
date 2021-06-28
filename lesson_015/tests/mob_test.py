import decimal
import unittest
import os
import dungeon_engine


class TestMob(unittest.TestCase):

    def setUp(self):
        os.chdir("..")
        self.dungeon = dungeon_engine.load_dungeon()
        self.game = dungeon_engine.Gameplay('123456.0987654321')
        os.chdir("tests")
        self.game.current_location.mobs = [dungeon_engine.Monster("Mob_exp30_tm30")]

    def test_mob(self):
        monster = dungeon_engine.Monster("Mob_exp30_tm30")
        self.assertEqual(self.game.current_location.mobs, [monster])

    def test_mob_fight(self):
        exp = 30
        remaining_time = decimal.Decimal('123426.0987654321')
        time_passed = decimal.Decimal("30")
        self.game._fight()
        self.assertEqual(self.game.hero.exp, exp)
        self.assertEqual(remaining_time, self.game.hero.time_left)
        self.assertEqual(time_passed, self.game.hero.time_passed)
        self.assertEqual(0, len(self.game.current_location.mobs))


if __name__ == "__main__":
    TestMob()
