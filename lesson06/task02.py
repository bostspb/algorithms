"""
Подсчитать, сколько было выделено памяти под переменные

Задача №2 из урока №3
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random
from memory_info import MemoryInfo

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

result = []
en_array = enumerate(array)
for i, item in en_array:
    if item % 2 == 0:
        result.append(i)

memory_info = MemoryInfo()
memory_info.calc(SIZE)
memory_info.calc(MIN_ITEM)
memory_info.calc(MAX_ITEM)
memory_info.calc(array)
memory_info.calc(result)
memory_info.calc(i)
memory_info.calc(item)
memory_info.calc(en_array)

print(result)
memory_info.print_result()
