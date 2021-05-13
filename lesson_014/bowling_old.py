# -*- coding: utf-8 -*-


class LengthError(ValueError):
    pass


class IncorrectSymbols(ValueError):
    pass


class ContainsZeroError(ValueError):
    pass


class UnpairedScore(ValueError):
    pass


class IncorrectPair(ValueError):
    pass


class TooManyRounds(ValueError):
    pass


class FirstSlashError(ValueError):
    pass


class SecondStrikeError(ValueError):
    pass


def get_score(game_result):
    counter = ScoreCounter(game_result)
    return counter.count_score()


class ScoreCounter:
    def __init__(self, value):
        self.result = str(value)
        self.score = 0

    def count_score(self):
        self.result = self.result.replace("Х", "X")
        self._check_result()
        pair_maker = PairMaker(self.result)
        pairs = pair_maker.make_pairs()
        for pair in pairs:
            if isinstance(pair, tuple):
                if sum(pair) > 9:
                    raise IncorrectPair("Некорректная пара: сбиты все кегли, должен быть знак \"/\"")
                self.score += sum(pair)
            else:
                self.score += pair
        return self.score

    def _check_result(self):
        if 10 > len(self.result):
            raise LengthError(f"Некорректная длина значения: слишком мало символов: {len(self.result)}")
        if 20 < len(self.result):
            raise LengthError(f"Некорректная длина значения: слишком много символов: {len(self.result)}")
        if "0" in self.result:
            raise ContainsZeroError("Есть 0. Вместо него необходимо использовать \"-\"")


class PairMaker:
    def __init__(self, value):
        self.value = str(value).replace("-", "0")
        self.pairs = []
        self.pair_score = 0
        self.current_pair = []

    def make_pairs(self):
        for symbol in self.value:
            self.pair_score += 1
            if symbol == "X":
                if self.pair_score > 1:
                    raise SecondStrikeError("Второе значение в паре - Х")
                self.current_pair = 20
                self._append_pair()
                continue
            self.current_pair.append(symbol)
            if self.pair_score == 2:
                if symbol == "/":
                    self.current_pair = 15
                self._append_pair()
            else:
                if symbol == "/":
                    raise FirstSlashError("Результат первого броска - \"/\"")
        if self.pair_score > 0:
            raise UnpairedScore("Есть непарные значения")
        self._check_rounds()
        return self.pairs

    def _append_pair(self):
        if isinstance(self.current_pair, list):
            for index in range(len(self.current_pair)):
                try:
                    self.current_pair[index] = int(self.current_pair[index])
                except ValueError:
                    raise IncorrectSymbols("Содержатся некорректные символы")
            self.pairs.append(tuple(self.current_pair))
        else:
            self.pairs.append(self.current_pair)
        self.pair_score = 0
        self.current_pair = []

    def _check_rounds(self):
        if len(self.pairs) > 10:
            raise TooManyRounds("Некорректное значение: введены данные для более чем 10 раундов")