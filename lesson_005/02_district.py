# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from pprint import pprint

from district.central_street.house1 import room1 as central_1_1
from district.central_street.house1 import room2 as central_1_2
from district.central_street.house2 import room1 as central_2_1
from district.central_street.house2 import room1 as central_2_2
from district.soviet_street.house1 import room1 as soviet_1_1
from district.soviet_street.house1 import room2 as soviet_1_2
from district.soviet_street.house2 import room1 as soviet_2_1
from district.soviet_street.house2 import room1 as soviet_2_2

# можно было сделать вот так:
district_rooms = (central_1_1.folks
                  + central_1_2.folks
                  + central_2_1.folks
                  + central_2_2.folks
                  + soviet_1_1.folks
                  + soviet_1_2.folks
                  + soviet_2_1.folks
                  + soviet_2_2.folks)

# print('На районе живут: ', ', '.join(district_rooms))
pprint('На районе живут: '+', '.join(district_rooms))


# for room in district_rooms:
#     if room is district_rooms[-1]:
#         people = ", "
#         people = people.join(room.folks)
#         print(people, end=".")
#     elif len(room.folks) > 0:
#         people = ", "
#         people = people.join(room.folks)
#         print(people, end=", ")
#     else:
#         continue

# print("На районе живут:", district_folks)

# зачет!
