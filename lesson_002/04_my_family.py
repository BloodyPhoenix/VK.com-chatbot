#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_famliy = ["Андрей", "Елена", "Александр", "Мария", "Валентина"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [["Андрей", 175], ["Елена", 165], ["Александр", 185], \
                    ["Мария", 175], ["Валентина", 160]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

# TODO Нет необходимости преобразовывать число к типу стринг, функция принт выводит все типы, используйте (,)
print("Рост отца: "+str(my_family_height[0][1]))
summ_height=0
# TODO тут у нас нейминг, напишите полностью что мы тут получаем!
for h in my_family_height:
    summ_height+=(h[1])
# TODO Нет необходимости преобразовывать число к типу стринг, функция принт выводит все типы, используйте (,)
print("Общий рост моей семьи: "+str(summ_height))