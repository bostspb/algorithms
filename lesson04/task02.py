"""
Задача №2
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

_Первый_ — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

_Второй_ — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

Пример работы программ:
sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
"""


def test_func(func):
    assert func(1) == 2
    print('Test 1 OK')
    assert func(4) == 7
    print('Test 2 OK')
    assert func(14) == 43
    print('Test 3 OK')
    assert func(42) == 181
    print('Test 4 OK')


def get_prime_number_position_via_sieve_of_eratosthenes(position):
    n = position ** 2 + 3
    sieve = [i for i in range(n + 1)]
    sieve[1] = 0
    current_position = 1
    for i in range(2, n + 1):
        if sieve[i] != 0:
            if current_position == position:
                return sieve[i]
            current_position += 1
            j = i + i
            while j <= n:
                sieve[j] = 0
                j += i


def get_prime_number_position(position):
    test_number = 2
    current_position = 0
    while current_position < position:
        is_prime = True
        for j in range(2, test_number):
            if test_number % j == 0:
                is_prime = False
                break
        if is_prime:
            current_position += 1
            prime_number = test_number
        test_number += 1
    return prime_number


c = get_prime_number_position(5)
print(c)
test_func(get_prime_number_position)


