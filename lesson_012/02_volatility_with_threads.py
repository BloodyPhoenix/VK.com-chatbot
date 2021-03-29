# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import utilities
from time import sleep
from threading import Thread


class VolatileCounter(Thread):
    # TODO принимаем еще арги и кварки
    def __init__(self, path):
        # TODO тут аналогично запускаем super с ними
        super().__init__()
        self.current_file = path
        self.volatility = None
        self.ticket_name = None

    def run(self):
        # TODO это тормозит выполнение, убрать
        sleep(0.01)
        prices = self.get_prices()
        self.get_volatility(prices)

    def get_prices(self):
        prices = set()
        with open(self.current_file, "r", encoding="utf-8") as ticker_data:
            for line in ticker_data:
                name, _, price, _ = line.split(",")
                if name == "SECID":
                    continue
                prices.add(float(price))
        prices = list(sorted(prices, reverse=True))
        self.ticket_name = name
        return prices

    def get_volatility(self, prices):
        max_price = prices[0]
        min_price = prices[-1]
        half_summ = (max_price + min_price) / 2
        self.volatility = ((max_price - min_price) / half_summ) * 100
        self.volatility = round(self.volatility, 2)


@utilities.time_track
def main():
    files = utilities.get_files("trades")
    counters = []
    volatilities = []
    zero_volailities = []
    for file in files:
        counters.append(VolatileCounter(file))
    for counter in counters:
        counter.run()

    # TODO нужно запустить еще один цикл с join()
    for counter in counters:
        name = counter.ticket_name
        volatility = counter.volatility
        if volatility == 0:
            zero_volailities.append(name)
        else:
            volatilities.append((name, volatility))
    utilities.check_volatility(volatilities, zero_volailities)


# TODO добавить время выполнения в первой и во второй части задания
if __name__ == "__main__":
    main()
