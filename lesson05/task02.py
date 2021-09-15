"""
Задача №2
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями `hex()` и/или `int()` для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.

Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""

from collections import deque

TO_DECIMAL = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
}
FROM_DECIMAL = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
}


def test_hex_operations():
    sum_ = hex_sum(['a', '2'], ['c', '4', 'f'])
    assert sum_ == ['c', 'f', '1']
    print(f'Test Sum OK')

    multiplication = hex_multiplication(['a', '2'], ['c', '4', 'f'])
    assert multiplication == ['7', 'c', '9', 'f', 'e']
    print(f'Test Multiplication OK')


def hex_sum(a, b):
    result = deque()
    base = len(TO_DECIMAL)

    if len(b) > len(a):
        a, b = deque(b), deque(a)
    else:
        a, b = deque(a), deque(b)

    memory = 0
    while len(a) > 0:
        if len(b) > 0:
            sum_ = TO_DECIMAL[a.pop()] + TO_DECIMAL[b.pop()] + memory
        else:
            sum_ = TO_DECIMAL[a.pop()] + memory

        if sum_ >= base:
            result.appendleft(FROM_DECIMAL[sum_ - base])
            memory = 1
        else:
            result.appendleft(FROM_DECIMAL[sum_])
            memory = 0

    if memory > 0:
        result.appendleft(memory)

    return list(result)


def hex_multiplication(a, b):
    base = len(TO_DECIMAL)

    if len(b) > len(a):
        a, b = deque(b), deque(a)
    else:
        a, b = deque(a), deque(b)

    zeroes = 0
    summands = list()
    while len(b) > 0:
        aa = a.copy()
        summand = deque()
        multiplier = TO_DECIMAL[b.pop()]
        memory = 0
        while len(aa) > 0:
            mul_dec = multiplier * TO_DECIMAL[aa.pop()] + memory
            if mul_dec >= base:
                memory = mul_dec // base
                digit = mul_dec % base
            else:
                memory = 0
                digit = mul_dec

            summand.appendleft(FROM_DECIMAL[digit])

        if memory > 0:
            summand.appendleft(FROM_DECIMAL[memory])

        summand.extend(['0'] * zeroes)
        summands.append(list(summand))
        zeroes += 1

    sum_ = summands.pop()
    while len(summands) > 0:
        summand = summands.pop()
        sum_ = hex_sum(sum_, summand)

    return sum_


first_number = input('Enter a first number:\n').lower()
second_number = input('Enter a second number:\n').lower()

print(f'{first_number} + {second_number} = ', *hex_sum(list(first_number), list(second_number)))
print(f'{first_number} * {second_number} = ', *hex_multiplication(list(first_number), list(second_number)))
