# -*- coding: utf-8 -*-

import os


def get_files(path):
    files = os.listdir(path)
    for index, file in enumerate(files):
        file = os.path.join(path, file)
        files[index] = file
    return files

def time_track(func, *args, **kwargs):
    started_at = time.time()

    result = func(*args, **kwargs)

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return result

def print_result(result):
    pass