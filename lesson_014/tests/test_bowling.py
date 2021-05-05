# -*- coding: utf-8 -*-

import unittest
from lesson_014 import bowling


class ScoreCounterTest(unittest.TestCase):

    def test_normal(self):
        score = bowling.get_score("X45-74/44X-927-4X")
        result = 121
        self.assertEqual(result, score)

    def test_length_short(self):
        with self.assertRaises(ValueError):
            bowling.get_score("34577")

    def test_length_long(self):
        with self.assertRaises(ValueError):
            bowling.get_score("X45-74/44X-927-4X3")

    def test_incorrect_symbols(self):
        with self.assertRaises(ValueError):
            bowling.get_score("XV5-74/44X-927-4X")

    def test_zero(self):
        with self.assertRaises(ValueError):
            bowling.get_score("X45074/44X-927-4X")

    def test_double_slash(self):
        with self.assertRaises(ValueError):
            bowling.get_score("X45-74//4X-927-4X")

    def test_pairs(self):
        with self.assertRaises(ValueError):
            bowling.get_score("X5-74/44X-927-4X")

    def test_more_that_eight(self):
        with self.assertRaises(ValueError):
            bowling.get_score("X65-74/44X-927-4X")


if __name__ == "__main__":
    tests = ScoreCounterTest()


