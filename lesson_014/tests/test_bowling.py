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

# TODO дописать тесты на переполнение, на недополнение, на ноль. + такие тесты как к примеру:
# TODO 'X4/341412X513/1-X'
# TODO 'X4/-41-12X5-3/1--9'
# TODO '99999999999999999999'
# TODO 'X4/-41-79X5-3/1--9'
# TODO '--------------------'
# TODO '-/-/-/-/-/-/-/-/-/-/'
# TODO 'XXXXXXXXXX'
# TODO '2/4/6/8/1/3/5/7/9/1/'
# TODO '/2/4/6/8/1/3/5/7/9/1'
# TODO 'qwerasdfzxcvtyghbnui'
# TODO '2/4/6/8/1/3/5/7/9/1/X'
# TODO '2/4/6/8/1/3/5/7/9/1'
# TODO ''
# TODO чем больше тестов тем лучше
