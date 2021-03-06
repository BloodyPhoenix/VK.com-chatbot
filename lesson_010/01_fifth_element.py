# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as ex:
    print(f"Ошибка {ex}. Пятый элемент не является числом")
except IndexError as ex:
    print(f"Ошибка {ex}. Отсутствует пятый элемент")
except Exception as ex:
    print(f"Что-то пошло не так. Исключение {ex} с параметрами {ex.args}")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

# зачет!
