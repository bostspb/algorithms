"""
Задача №4
Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

int_from, int_to = int(input('Enter the minimum integer\n')), int(input('Enter the maximum integer\n'))
int_random = random.randint(int_from, int_to)
print(f'Random integer: {int_random}')

float_from, float_to = float(input('Enter the minimum real number\n')), float(input('Enter the maximum real number\n'))
float_random = random.uniform(float_from, float_to)
print(f'Random real number: {float_random}')

letter_from, letter_to = input('Enter the letter from\n'), input('Enter the letter to\n')
letter_from_ordinal = ord(letter_from)
letter_to_ordinal = ord(letter_to)
letter_random_ordinal = random.randint(letter_from_ordinal, letter_to_ordinal)
letter_random = chr(letter_random_ordinal)
print(f'Random letter: {letter_random}')

