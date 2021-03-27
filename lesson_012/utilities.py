# -*- coding: utf-8 -*-

import os
import time


def get_files(path):
    files = os.listdir(path)
    for index, file in enumerate(files):
        file = os.path.join(path, file)
        files[index] = file
    return files


def time_track(func, *args, **kwargs):
    started_at = time.time()

    def decorated_func():
        result = func(*args, **kwargs)
        return result

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 2)
    print(f'Функция работала {elapsed} секунд(ы)')
    return decorated_func


def check_volatility(volatilities, zero_volatilities):
    sorted_volatilities = sorted(volatilities, key=lambda x: x[1], reverse=True)
    max_volatilities = sorted_volatilities[:3]
    min_volatilities = sorted_volatilities[-3:]
    print("Максимлальная волатильность:")
    print_result(max_volatilities)
    print("Минимальная волатильность:")
    print_result(min_volatilities)
    print("Нулевая волатильность:")
    print_result(zero_volatilities)


def print_result(result: list):
    for item in result:
        if isinstance(item, tuple):
            print(*item)
        else:
            if not item == result[-1]:
                print(item, end=", ")
            else:
                print(item)