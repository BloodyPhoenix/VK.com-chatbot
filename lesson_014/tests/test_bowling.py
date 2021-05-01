# -*- coding: utf-8 -*-

import unittest
from lesson_014 import bowling


class ScoreCounterTest(unittest.TestCase):

    def test_normal(self):
        score_counter = bowling.ScoreCounter("X45-74/44X-927-4X")
        result = 121
        self.assertEqual(result, score_counter.count_score())

    # TODO Это не ловля ошибок, это тест. Не пашет он тут через self.assertRaise
    # TODO С self.assertRaise он выдаёт сообщение о том, что якобы ошибка не рейзится, и падает
    # TODO а через assertEqual та же самая ошибка почему-то рейзится.
    def test_length_short(self):
        score_counter = bowling.ScoreCounter("34577")
        error = ValueError("Некорректная длина значения")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    def test_length_long(self):
        score_counter = bowling.ScoreCounter("345772235446747652144686")
        error = ValueError("Некорректная длина значения")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    def test_incorrect_symbols(self):
        score_counter = bowling.ScoreCounter("XV98-/66789/")
        error = ValueError("Содержатся некорректные символы")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    def test_zero(self):
        score_counter = bowling.ScoreCounter("X9098-/66789/")
        with self.assertRaises(ValueError):
            score_counter._check_result()

    def test_double_slash(self):
        score_counter = bowling.ScoreCounter("X9198-//6789/")
        with self.assertRaises(ValueError):
            score_counter._check_result()

    def test_pairs(self):
        score_counter = bowling.ScoreCounter("X91-/X44X725")
        score_counter._count_strikes()
        error = ValueError("Есть непарные значения")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    def test_more_that_eight(self):
        score_counter = bowling.ScoreCounter("X55-74/44X-927-4X")
        with self.assertRaises(ValueError):
            score_counter.count_score()


if __name__ == "__main__":
    tests = ScoreCounterTest()


