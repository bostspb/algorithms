"""
Задача №1
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = int(input('Enter a three-digit number\n'))

digit_1 = number % 10
digit_2 = number // 10 % 10
digit_3 = number // 10 // 10 % 10

my_pow = digit_1 * digit_2 * digit_3
my_sum = digit_1 + digit_2 + digit_3

print(f"{digit_1} * {digit_2} * {digit_3} = {my_pow}")
print(f"{digit_1} + {digit_2} + {digit_3} = {my_sum}")

