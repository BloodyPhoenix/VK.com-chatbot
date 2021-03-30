# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
import multiprocessing
import queue


class VolatileCounter(multiprocessing.Process):
    def __init__(self, path, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_file = path
        self.collector = collector
        self.volatility = None
        self.ticket_name = None

    def run(self):
        prices = self.get_prices()
        self.get_volatility(prices)
        self.collector.put((self.name, self.volatility))

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
    collector = multiprocessing.Queue(maxsize=2)
    counters = []
    volatilities = []
    zero_volailities = []
    for file in files:
        counters.append(VolatileCounter(file, collector))
    for counter in counters:
        counter.start()
    while True:
        try:
            name, volatility = collector.get(timeout=0.1)
            if volatility == 0:
                zero_volailities.append(name)
            else:
                volatilities.append((name, volatility))
        except queue.Empty:
            if not any(counter.is_alive() for counter in counters):
                break
    for counter in counters:
        counter.join()
    utilities.check_volatility(volatilities, zero_volailities)


# время выполнения 1,77-1,49 секунд
if __name__ == "__main__":
    main()
