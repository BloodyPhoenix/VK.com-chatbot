#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!



term = len("Терминатор")
five = len("Пятый элемент")
alien = len("Чужие")
future = len("Назад в будущее")


print(my_favorite_movies[0:term])
print(my_favorite_movies[-future:-1])
print(my_favorite_movies[(term+2):(term+2+five)])
print(my_favorite_movies[(-future-2-alien):(-future-2)])


