# -*- coding: utf-8 -*-

import unittest
from lesson_014 import bowling


class ScoreCounterTest(unittest.TestCase):

    def test_normal(self):
        "Tests normal input"
        score = bowling.get_score("X45-74/44X-927-4X")
        result = 121
        self.assertEqual(result, score)

    def test_length_short(self):
        "Tests if lengnth is less than 10"
        with self.assertRaises(bowling.LengthError):
            bowling.get_score("X45-74/44")

    def test_length_long(self):
        "Tests if length more than 20"
        with self.assertRaises(bowling.LengthError):
            bowling.get_score("X45-74/44X-927-4XX45-74/44X-927-4X")

    def test_incorrect_symbols(self):
        "Tests if there are incorrect symbols other than zero"
        with self.assertRaises(bowling.IncorrectSymbols):
            bowling.get_score("X4t-74/44X-927-4X")

    def test_zero(self):
        "Tests if score contains zero"
        with self.assertRaises(bowling.ContainsZeroError):
            bowling.get_score("X45074/44X-927-4X")

    def test_double_slash(self):
        "Tests if there are double slashes"
        with self.assertRaises(bowling.DoubleSlash):
            bowling.get_score("X45-74//4X-927-4X")

    def test_pairs(self):
        "Tests if there unpaired meanings"
        with self.assertRaises(bowling.UnpairedScore):
            bowling.get_score("X5-74/44X-927-4X")

    def test_more_that_eight(self):
        """Tests if there a pair with sum 10 or more"""
        with self.assertRaises(bowling.IncorrectPair):
            bowling.get_score("X75-74/44X-927-4X")

    def test_too_many_pairs(self):
        """Tests if there are too many rounds"""
        with self.assertRaises(bowling.TooManyRounds):
            bowling.get_score("XXX-74/44X-927-4X")


if __name__ == "__main__":
    tests = ScoreCounterTest()
