#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, "bear")
print(*zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
#  и выведите список на консоль
# TODO используйте просто метод extend
for b in birds:
    zoo.extend(b)
print(*zoo)

# уберите слона
#  и выведите список на консоль

zoo.remove("elephant")
print(*zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

real_lion = zoo.index("lion")+1
real_lark = zoo.lark("lark")+1

print("Лев сидит в клетке номер "+real_lion)
print("Жаворонок сидит в клетке "+real_lark)

# TODO код падает с ошибкой исправить!
