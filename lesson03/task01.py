"""
Задача №1
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
numbers = [z for z in range(2, 10)]
counts = [0 for _ in range(8)]
i = 0
for m in range(2, 10):
    for n in range(2, 100):
        if n % m == 0:
            counts[i] += 1
    print(f'The set (2..99) contains {counts[i]} numbers that are multiples of {numbers[i]}')
    i += 1
