# -*- coding: utf-8 -*-
import re


def get_score(game_result):
    counter = ScoreCounter(game_result)
    return counter.count_score()


class ScoreCounter:
    def __init__(self, value):
        self.result = str(value)
        self.strikes = 0
        self.pairs = []
        self.score = 0

    def count_score(self):
        self.result = self.result.replace("Х", "X")
        self._check_result()
        self._count_strikes()
        self._check_pairs()
        self._make_pairs()
        self.score += self.strikes*20
        for pair in self.pairs:
            if "/" in pair:
                self.score += 15
            else:
                pair_result = int(pair[0])+int(pair[1])
                if pair_result > 9:
                    # TODO тобы каждый раз у вам не ловить одну и туже ошибку нужно их костамихировать
                    # TODO и отнаследоваться от ValueError
                    # TODO так по названию класса можно будет определить что за ошибка сейчас сработала
                    raise ValueError("Некорректная пара: сбиты все кегли, должен быть знак \"/\"")
                self.score += pair_result
        return self.score

    def _check_result(self):
        if 10 >= len(self.result) >= 20:
            raise ValueError("Некорректная длина значения")
        if re.match(r"[^1-9X\-/]+", self.result):
            raise ValueError("Содержатся некорректные символы")
        if "0" in self.result:
            raise ValueError("Есть 0. Вместо него необходимо использовать \"-\"")
        if "/" in self.result:
            for index, symbol in enumerate(self.result):
                if symbol == "/":
                    if self.result[index-1] == "/":
                        raise ValueError("Два символа \"/\" подряд")

    def _count_strikes(self):
        for symbol in self.result:
            if symbol == "X":
                self.strikes += 1

    def _check_pairs(self):
        if (len(self.result)-self.strikes)%2 != 0:
            raise ValueError("Есть непарные значения")

    def _make_pairs(self):
        current_index = 0
        while current_index < len(self.result):
            symbol = self.result[current_index]
            if symbol == "X":
                current_index += 1
            else:
                if symbol == "-":
                    symbol = "0"
                self.pairs.append((symbol, self.result[current_index+1]))
                current_index += 2
