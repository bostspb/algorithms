"""
Задача №3
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_position = 0
min_position = 0
for i, item in enumerate(array):
    if item > array[max_position]:
        max_position = i
    if item < array[min_position]:
        min_position = i

print(max_position, min_position)

array[max_position], array[min_position] = array[min_position], array[max_position]
print(array)
