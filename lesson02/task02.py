"""
Задача №2
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

even_count = 0
odd_count = 0

orig_number = number = int(input('Enter a number:\n'))

while number != 0:
    digit = number % 10
    if digit == 1 or digit == 3 or digit == 5 or digit == 7 or digit == 9:
        odd_count += 1
    else:
        even_count += 1
    number //= 10

print(f'The number {orig_number} is consist {even_count} even digits and {odd_count} odd digits.')