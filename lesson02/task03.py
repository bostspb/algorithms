"""
Задача №3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

number = int(input('Enter a number:\n'))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f'Reversed number is {reversed_number}')