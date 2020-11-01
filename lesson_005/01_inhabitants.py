# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1, room_2

room_1_folks = ", "
room_1_folks = room_1_folks.join(room_1.folks)

room_2_folks = ", "
room_2_folks = room_2_folks.join(room_2.folks)

print("В комнате room_1 живут:", room_1_folks)
print("В комнате room_2 живут:", room_2_folks)


# зачет!
