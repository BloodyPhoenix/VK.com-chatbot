# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ground):
            return Lava()
        else:
            return None


class Ground:
    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    def __str__(self):
        return "Шторм"


class Steam:
    def __str__(self):
        return "Пар"


class Dirt:
    def __str__(self):
        return "Грязь"

    def __add__(self, other):
        if isinstance(other, Water):
            return Swamp()
        elif isinstance(other, Air):
            return Sand()
        elif isinstance(other, Fire):
            return Clay()


class Lightning:
    def __str__(self):
        return "Молния"

    def __add__(self, other):
        if isinstance(other, Water):
            return Life()
        else:
            return None


class Dust:
    def __str__(self):
        return "Пыль"


class Lava:
    def __str__(self):
        return "Лава"

    def __add__(self, other):
        if isinstance(other, Water):
            return Stone()
        else:
            return None


class Life:
    def __str__(self):
        return "Жизнь"

    def __add__(self, other):
        if isinstance(other, Water):
            return Plankton()
        elif isinstance(other, Fire):
            return Ash()
        elif isinstance(other, Ground):
            return Moss()


class Stone:
    def __str__(self):
        return "Камень"


class Ash:
    def __str__(self):
        return "Пепел"


class Clay:
    def __str__(self):
        return "Глина"


class Moss:
    def __str__(self):
        return "Мох"


class Swamp:
    def __str__(self):
        return "Болото"


class Sand:
    def __str__(self):
        return "Песок"


class Plankton:
    def __str__(self):
        return "Планктон"


print(Water(), "+", Ground(), "=", Water()+Ground(), "+", Fire(), "=", Water() + Ground() + Fire())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# зачет!
