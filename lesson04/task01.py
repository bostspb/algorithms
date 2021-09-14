"""
Задача №1
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
- выбрать хорошую задачу, которую имеет смысл оценивать,
- написать 3 варианта кода (один у вас уже есть),
- проанализировать 3 варианта и выбрать оптимальный,
- результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
- написать общий вывод: какой из трёх вариантов лучше и почему.
"""


# Задача №4 из урока №3: Определить, какое число в массиве встречается чаще всего.

import random
import cProfile
import timeit

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10

array_10 = [random.randint(0, 50) for _ in range(10)]
array_50 = [random.randint(0, 50) for _ in range(50)]
array_100 = [random.randint(0, 50) for _ in range(100)]
array_500 = [random.randint(0, 50) for _ in range(500)]
array_1000 = [random.randint(0, 50) for _ in range(1000)]


def test_func(func):
    print(func)
    test_array = [3, 3, 0, 4, 4, 1, 6, 2, 9, 6, 1, 7, 3, 3, 1, 10, 6, 4, 6, 8]
    result = func(test_array)
    assert result[0] == 3
    assert result[1] == 4
    print(f'Test 1 OK')

    test_array = [3, 0, 2, 7, 1, 6, 8, 1, 3, 10, 0, 3, 9, 1, 1, 6, 1]
    result = func(test_array)
    assert result[0] == 1
    assert result[1] == 5
    print(f'Test 2 OK\n')


# С двумя циклами
def get_most_frequent_number_01(array):
    best_position = 0
    best_count = 1
    array_size = len(array)
    for i in range(array_size):
        count = 1
        for j in range(array_size):
            if i != j and array[i] == array[j]:
                count += 1
        if count > best_count:
            best_count = count
            best_position = i
    return [array[best_position], best_count]


# С двумя циклами с оптимизацией
def get_most_frequent_number_02(array):
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
    return [array[best_position], best_count]


# С одним циклом
def get_most_frequent_number_03(array):
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    return [num, frequency]


def print_time(f_name):
    print('#### PRINT TIME FOR FUNTION ' + f_name + ' ####')
    print(timeit.timeit(f_name + '(array_10)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(array_50)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(array_100)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(array_500)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(array_1000)', number=100, globals=globals()))
    print('')


def print_profile(f_name):
    print('==== PRINT PROFILE FOR FUNTION ' + f_name + ' ====')
    cProfile.run(f_name + '(array_10)')
    cProfile.run(f_name + '(array_50)')
    cProfile.run(f_name + '(array_100)')
    cProfile.run(f_name + '(array_500)')
    cProfile.run(f_name + '(array_1000)')
    print('')


def main():
    test_func(get_most_frequent_number_01)
    test_func(get_most_frequent_number_02)
    test_func(get_most_frequent_number_03)

    print('Example (get_most_frequent_number_01):')
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)
    result = get_most_frequent_number_01(array)
    print(f'The number {result[0]} occurs most often: {result[1]} times.\n\n')

    print_time('get_most_frequent_number_01')
    print_time('get_most_frequent_number_02')
    print_time('get_most_frequent_number_03')

    print_profile('get_most_frequent_number_01')
    print_profile('get_most_frequent_number_02')
    print_profile('get_most_frequent_number_03')


main()

"""
Результаты замеров находятся в файле task01_log.txt
Анализируя код алгоритмов, можно сделать вывод, что у первых двух алгоритмов будет квадратичная сложность O(N^2), 
т.к. там используется два вложенных цикла, а у алгоритма с одним циклом - линейная сложность O(N). 
Сделанные выводы подтверждаются результатами замеров.
Профайлинг функций не выявил явных проблем, кроме медленной скорости выполнения в первых двух фукциях при N > 500
"""