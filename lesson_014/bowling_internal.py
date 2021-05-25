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
        self.state = 1
        self.pairs = 0
        self.score = 0
        self.pair_counter = 0
        self.current_pair_score = 0
        self.current_pair = 0
        self.current_symbol = None

    def count_score(self):
        self.result = self.result.replace("Х", "X")
        self._check_result()
        for symbol in self.result:
            self.current_symbol = symbol
            if self.current_symbol == "-":
                self.current_symbol = 0
            self.check_state()
        if self.current_pair > 0:
            raise UnpairedScore("Есть непарные значения")
        return self.score

    def check_state(self):
        if self.state == 1:
            state_object = self.first_roll()
        else:
            state_object = self.second_roll()
        roll_result = state_object.count_roll()
        if roll_result == 20 or roll_result == 15:

            self.state = 1
            self.current_pair = 0
            self.current_pair_score = 0
            self.score += roll_result
            return
        if self.current_pair < 2:
            self.current_pair_score += roll_result
            self.current_pair += 1
            if self.current_pair_score > 9:
                raise IncorrectPair("Некорректная пара: сбиты все кегли, должен быть знак \"/\"")
        if self.current_pair == 2:
            self.current_pair = 0
            self.score += self.current_pair_score
            self.current_pair_score = 0
            self.state = 1
            return

    def first_roll(self):
        self.pair_counter += 1
        if self.pair_counter > 10:
            raise TooManyRounds("Некорректное значение: введены данные для более чем 10 раундов")
        self.state = 2
        return FirstRoll(self.current_symbol)

    def second_roll(self):
        return SecondRoll(self.current_symbol)

    def _check_result(self):
        if 10 > len(self.result):
            raise LengthError(f"Некорректная длина значения: слишком мало символов: {len(self.result)}")
        if 20 < len(self.result):
            raise LengthError(f"Некорректная длина значения: слишком много символов: {len(self.result)}")
        if "0" in self.result:
            raise ContainsZeroError("Есть 0. Вместо него необходимо использовать \"-\"")


class CountRoll:
    def __init__(self, roll):
        self.roll = roll

    def count_roll(self):
        pass


class FirstRoll(CountRoll):

    def count_roll(self):
        self._check_symbol()
        if self.roll == "X":
            return 20
        else:
            try:
                result = int(self.roll)
                return result
            except ValueError:
                raise IncorrectSymbols("Содержатся некорректные символы")

    def _check_symbol(self):
        if self.roll == "/":
            raise FirstSlashError("Результат первого броска - \"/\"")


class SecondRoll(CountRoll):

    def count_roll(self):
        self._check_symbol()
        if self.roll == "/":
            return 15
        else:
            try:
                result = int(self.roll)
                return result
            except ValueError:
                raise IncorrectSymbols("Содержатся некорректные символы")

    def _check_symbol(self):
        if self.roll == "X":
            raise SecondStrikeError("Результат второго броска - \"Х\"")


class Strike(CountRoll):

    def count_roll(self):
        result = 10
        self._check_symbol()
        next_rolls = self.roll[1:3]
        if "/" in next_rolls:
            result += 10
            return result
        for roll in next_rolls:
            if "X" == roll:
                result += 10
            else:
                result += int(roll)

    def _check_symbol(self):
        if self.roll[1] == "/":
            raise FirstSlashError("Результат первого броска - \"/\"")


class Spare(CountRoll):

    def count_roll(self):
        pass

    def _check_symbol(self):
        if self.roll[1] == "/":
            raise FirstSlashError("Результат первого броска - \"/\"")
