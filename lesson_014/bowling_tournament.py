# -*- coding: utf-8 -*-


import bowling
import os


class NotATxtFileError(ValueError):
    pass


def count_tournament_result(result):
    if not str(result).endswith(".txt"):
        raise NotATxtFileError("Неверный формат файла. Поддерживаются только файлы в формате .txt")
    counter = TournamentCounter(result)
    counter.make_result()


class TournamentCounter:
    def __init__(self, result):
        self.result = result
        self.current_tour = None
        self.current_winner = None
        self.current_tournament = []
        self.current_results = []

    def make_result(self):
        self._count_tournament()

    def _write_result(self):
        with open("tournament_result.txt", "a") as t_result:
            t_result.write(self.current_tour)
            for player in self.current_tournament:
                output = "{:<10} {:^20}, {:<3}\n".format(player[0], player[1], player[2])
                t_result.write(output)
            t_result.write(self.current_winner)
            t_result.write("\n\n")
        self._clear_current_tournament()

    def _clear_current_tournament(self):
        self.current_winner = None
        self.current_tour = None
        self.current_tournament = []
        self.current_results = []

    def _count_tournament(self):
        with open(self.result, "r") as incoming_data:
            for line in incoming_data:
                if line.startswith("###"):
                    self.current_tour = line
                elif line.startswith("winner"):
                    self._define_winner()
                    self._write_result()
                elif len(line) < 4:
                    continue
                else:
                    self._count_player_result(line)

    def _define_winner(self):
        max_score = max(self.current_results)
        winner = []
        for player, _, score in self.current_tournament:
            if max_score == score:
                winner.append(player)
        if len(winner) == 0:
            result = "nobody"
        elif len(winner) > 1:
            result = "draw:"
            for player in winner:
                result = " "+player
        else:
            result = "winner is "+winner[0]
        self.current_winner = result

    def _count_player_result(self, player_result):
        name, result = player_result.split()
        try:
            score = bowling.get_score(result)
        except ValueError as error:
            print(error, error.args)
            score = 0
        updated_result = (name, result, score)
        self.current_tournament.append(updated_result)
        self.current_results.append(score)