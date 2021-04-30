# -*- coding: utf-8 -*-

import unittest
from lesson_014 import bowling


class ScoreCounterTest(unittest.TestCase):

    def test_normal(self):
        score_counter = bowling.ScoreCounter("X45-74/44X-927-4X")
        result = 121
        self.assertEqual(result, score_counter.count_score())

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

    # TODO Почему-то этот тест падает при том, что текст сообщения скопирован из основного модуля
    def test_zero(self):
        score_counter = bowling.ScoreCounter("X9098-/66789/")
        error = ValueError("Есть 0. Вместо него необходимо использовать \"-\"")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    # TODO С этим то же самое
    def test_double_slash(self):
        score_counter = bowling.ScoreCounter("X9198-//6789/")
        error = ValueError("Два символа \"/\" подряд")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    def test_pairs(self):
        score_counter = bowling.ScoreCounter("X91-/X44X725")
        score_counter._count_strikes()
        error = ValueError("Есть непарные значения")
        try:
            score_counter._check_result()
        except ValueError as test_error:
            self.assertEqual(error, test_error)

    # TODO И здесь тоже. Полагаю, что дело в символах -/, так как именно тесты с ними падают. От кавычек это не зависит
    def test_more_that_eight(self):
        score_counter = bowling.ScoreCounter("X55-74/44X-927-4X")
        error = ValueError("Некорректная пара: сбиты все кегли, должен быть знак \"/\"")
        try:
            score_counter.count_score()
        except ValueError as test_error:
            self.assertEqual(error, test_error)


if __name__ == "__main__":
    tests = ScoreCounterTest()


