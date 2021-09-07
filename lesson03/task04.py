"""
Задача №4
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

best_position = 0
best_count = 1
array_size = len(array)
for i in range(array_size):
    count = 1
    for j in range(i + 1, array_size):
        if array[i] == array[j]:
            count += 1
    if count > best_count:
        best_count = count
        best_position = i

print(f'The number {array[best_position]} occurs most often: {best_count} times.')