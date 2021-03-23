# -*- coding: utf-8 -*-

import os
import time


def get_files(path):
    files = os.listdir(path)
    for index, file in enumerate(files):
        file = os.path.join(path, file)
        files[index] = file
    return files

# TODO доработать декоратор
def time_track(func, *args, **kwargs):
    started_at = time.time()

    def decorated_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return decorated_func


def print_result(result: list):
    for item in result:
        if isinstance(item, tuple):
            print(*item)
        else:
            if not item == result[-1]:
                print(item, end=", ")
            else:
                print(item)