# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as central_1_1
from district.central_street.house1 import room2 as central_1_2
from district.central_street.house2 import room1 as central_2_1
from district.central_street.house2 import room1 as central_2_2
from district.soviet_street.house1 import room1 as soviet_1_1
from district.soviet_street.house1 import room2 as soviet_1_2
from district.soviet_street.house2 import room1 as soviet_2_1
from district.soviet_street.house2 import room1 as soviet_2_2

district_rooms = [central_1_1, central_1_2, central_2_1, central_2_2, soviet_1_1, soviet_1_2, soviet_2_1, soviet_2_2]

# TODO попробуйте применить join без всего этого лишнего вычисления
district_folks = []

for room in district_rooms:
    district_folks += room.folks

formated_folks = ", "
formated_folks = formated_folks.join(district_folks)

print("На районе живут:", formated_folks)



