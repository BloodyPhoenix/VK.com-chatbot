# -*- coding: utf-8 -*-

import unittest
from lesson_014 import bowling


class ScoreCounterTest(unittest.TestCase):

    def test_normal_0(self):
        """Tests normal input"""
        score = bowling.get_score("Х45-74/44X-927-4X", "external")
        result = 108
        self.assertEqual(result, score)

    def test_normal_1(self):
        """Tests normal input"""
        score = bowling.get_score("1245-74/44X-92--4X", "external")
        result = 85
        self.assertEqual(result, score)

    def test_normal_2(self):
        """Tests normal input"""
        score = bowling.get_score("1245-74/4425-92--432", "external")
        result = 68
        self.assertEqual(result, score)

    def test_normal_no_strikes(self):
        """Tests normal input without strikes"""
        score = bowling.get_score("1245-74/4435-92--471", "external")
        result = 72
        self.assertEqual(result, score)

    def test_normal_numbers_only(self):
        """Tests normal input if there are no misses, spares or strikes"""
        score = bowling.get_score("12451744443518211471", "external")
        result = 69
        self.assertEqual(result, score)

    def test_normal_full_strike(self):
        """Tests if there are only strikes"""
        score = bowling.get_score("XXXXXXXXXX", "external")
        result = 270
        self.assertEqual(result, score)

    def test_normal_miss_only(self):
        """Tests if there are only misses"""
        score = bowling.get_score("--------------------", "external")
        self.assertEqual(0, score)

    def test_length_short(self):
        "Tests if lengnth is less than 10"
        with self.assertRaises(bowling.LengthError):
            bowling.get_score("X45-74/44", "external")

    def test_length_long(self):
        "Tests if length more than 20"
        with self.assertRaises(bowling.LengthError):
            bowling.get_score("X45-74/44X-927-4XX45-74/44X-927-4X", "external")

    def test_incorrect_symbols(self):
        "Tests if there are incorrect symbols other than zero"
        with self.assertRaises(bowling.IncorrectSymbols):
            bowling.get_score("X4t-74/44X-927-4X", "external")

    def test_zero(self):
        "Tests if score contains zero"
        with self.assertRaises(bowling.ContainsZeroError):
            bowling.get_score("X45074/44X-927-4X", "external")

    def test_pairs(self):
        "Tests if there unpaired meanings"
        with self.assertRaises(bowling.UnpairedScore):
            bowling.get_score("Х45-74/44X-927-48", "external")

    def test_more_that_eight(self):
        """Tests if there a pair with sum 10 or more"""
        with self.assertRaises(bowling.IncorrectPair):
            bowling.get_score("X75-74/44X-927-4X", "external")

    def test_too_many_pairs(self):
        """Tests if there are too many rounds"""
        with self.assertRaises(bowling.TooManyRounds):
            bowling.get_score("XXX-74/44X-927-4X", "external")

    def test_first_roll_slash(self):
        """Tests if there is a slash in a first roll"""
        with self.assertRaises(bowling.FirstSlashError):
            bowling.get_score("Х45-7/444X-927-4X", "external")

    def test_second_strike(self):
        """Tests if there is a strike as a second symbol in pair"""
        with self.assertRaises(bowling.SecondStrikeError):
            bowling.get_score("Х4X-74/44X-927-4X", "external")


if __name__ == "__main__":
    tests = ScoreCounterTest()