"""
Двоичный (бинарный) поиск, дихотомия

O(log n) действий, где n - количество элементов в массиве.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array.sort()
print(array)

find = int(input('Enter a number:\n'))

pos = len(array) // 2
left = 0
right = len(array) - 1
count = 1

while array[pos] != find and left <= right:
    count += 1
    if find > array[pos]:
        left = pos + 1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('Element is missed' if left > right else f'Element on position {pos}')
print(f'{count}')