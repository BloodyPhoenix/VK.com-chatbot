# -*- coding: utf-8 -*-


class LengthError(ValueError):
    pass


class IncorrectSymbols(ValueError):
    pass


class ContainsZeroError(ValueError):
    pass


class DoubleSlash(ValueError):
    pass


class UnpairedScore(ValueError):
    pass


class IncorrectPair(ValueError):
    pass


class TooManyRounds(ValueError):
    pass


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
        self._check_rounds()
        self.score += self.strikes*20
        for pair in self.pairs:
            if "/" in pair:
                self.score += 15
            else:
                try:
                    pair_result = int(pair[0])+int(pair[1])
                except ValueError:
                    raise IncorrectSymbols("Содержатся некорректные символы")
                if pair_result > 9:
                    raise
                self.score += pair_result
        return self.score

    def _check_result(self):
        if 10 > len(self.result):
            raise LengthError(f"Некорректная длина значения: слишком мало символов: {len(self.result)}")
        if 20 < len(self.result):
            raise LengthError(f"Некорректная длина значения: слишком много символов: {len(self.result)}")
        if "0" in self.result:
            raise ContainsZeroError("Есть 0. Вместо него необходимо использовать \"-\"")
        if "/" in self.result:
            for index, symbol in enumerate(self.result):
                if symbol == "/":
                    if self.result[index-1] == "/":
                        raise DoubleSlash("Два символа \"/\" подряд")

    def _count_strikes(self):
        for symbol in self.result:
            if symbol == "X":
                self.strikes += 1

    def _check_pairs(self):
        if (len(self.result)-self.strikes)%2 != 0:
            raise UnpairedScore("Есть непарные значения")

    def _make_pairs(self):
        current_index = 0
        while current_index < len(self.result):
            symbol = self.result[current_index]
            if symbol == "X":
                current_index += 1
            else:
                next_symbol = self.result[current_index+1]
                if symbol == "-":
                    symbol = "0"
                if next_symbol == "-":
                    next_symbol = "0"
                self.pairs.append((symbol, next_symbol))
                current_index += 2

    def _check_rounds(self):
        if len(self.pairs) + self.strikes > 10:
            raise TooManyRounds("Некорректное значение: введены данные для более чем 10 раундов")