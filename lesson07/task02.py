"""
Задача №2
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке `[0; 50)`.
Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array):
    # Отдаем отсортированный массив из одного элемента
    # и крайний случай - когда массив пустой
    if len(array) < 2:
        return array

    # Если в массиве больше одного элемента - разбиваем пополам
    middle = len(array) // 2
    left, right = array[:middle],  array[middle:]

    # Сортируем половинки
    left = merge_sort(left)
    right = merge_sort(right)

    # Слияние отсортированных половинок
    result = []
    # У каждой половинки заводим свой индекс
    li = ri = 0
    # Всего проходов будет как размер результирующего массива
    for _ in range(0, len(left) + len(right)):
        # Если мы уже обработали все элементы из левого массива,
        # то просто берем очередной элемент из правого массива
        if li > len(left) - 1:
            result.append(right[ri])
            ri += 1
        # Если мы уже обработали все элементы из правого массива,
        # то просто берем очередной элемент из левого массива
        elif ri > len(right) - 1:
            result.append(left[li])
            li += 1
        # Выбираем наименьший элемент из половинок, согласно текущим индексам
        elif left[li] > right[ri]:
            result.append(right[ri])
            # сдвигаем индекс использованного элемента
            ri += 1
        else:
            result.append(left[li])
            # сдвигаем индекс использованного элемента
            li += 1

    return result


if __name__ == '__main__':
    test_array = [random.uniform(0, 49.9999) for _ in range(10)]
    print(test_array)
    test_array_sorted = merge_sort(test_array)
    print(test_array_sorted)
