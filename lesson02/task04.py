"""
Задача №4
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Enter a count of elements:\n'))
element = 1
sum = 0

for _ in range(n):
    sum += element
    element /= -2

print(f'Sum of {n} elements: {sum}')