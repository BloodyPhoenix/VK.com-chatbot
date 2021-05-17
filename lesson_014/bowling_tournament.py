# -*- coding: utf-8 -*-


import bowling


class NotATxtFileError(ValueError):
    pass


def count_tournament_result(result, output_name=None):
    if not str(result).endswith(".txt"):
        raise NotATxtFileError("Неверный формат файла. Поддерживаются только файлы в формате .txt")
    counter = TournamentCounter(result, output_name)
    counter.make_result()


class TournamentCounter:
    def __init__(self, result, output_name):
        self.result = result
        self.current_tour = None
        self.current_winner = None
        self.current_tournament = []
        self.current_results = []
        self.current_player = None
        if output_name:
            self.output_file = output_name
        else:
            self.output_file = "tournament_result.txt"

    def make_result(self):
        self._count_tournament()

    def _write_result(self):
        with open(self.output_file, "a", encoding="utf8") as t_result:
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
                    try:
                        self._count_player_result(line)
                    except ValueError as error:
                        with open("tournament_errors.log", "a", encoding="utf8'") as log:
                            error_message = self.current_tour + " " + self.current_player + ": " \
                                            + str(error) + "\n" + "\n"
                            log.write(error_message)

    def _define_winner(self):
        try:
            max_score = max(self.current_results)
        except ValueError:
            with open("tournament_errors.log", "a", encoding="utf8'") as log:
                error_message = self.current_tour + "All results of this tour are invalid!"
                log.write(error_message)
            self.current_winner = "Unable to define winner due to incorrect input"
            return
        winner = []
        for player, _, score in self.current_tournament:
            if max_score == score:
                winner.append(player)
        if len(winner) == 0:
            result = "nobody"
        elif len(winner) > 1:
            result = "draw:"
            for player in winner:
                result = " " + player
        else:
            result = "winner is " + winner[0]
        self.current_winner = result

    def _count_player_result(self, player_result):
        self.current_player, result = player_result.split()
        score = bowling.get_score(result)
        updated_result = (self.current_player, result, score)
        self.current_tournament.append(updated_result)
        self.current_results.append(score)


if __name__ == "__main__":
    count_tournament_result("tournament.txt")
