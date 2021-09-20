"""
Задача №3
Массив размером `2m + 1`, где `m` — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""
import random


def get_median(array):
    for i in range(0, len(array)):
        more = less = 0
        for j in range(0, len(array)):
            if array[i] > array[j]:
                less += 1
            elif array[i] < array[j]:
                more += 1
            elif i != j:
                if less > more:
                    more += 1
                else:
                    less += 1
        if less == more:
            return array[i]

    return None


def test_median():
    # все элементы уникальны
    arr01 = [2, 6, 7, 4, 9, 1, 3]
    print(get_median(arr01))
    assert get_median(arr01) == 4
    print('Test #1 OK')

    # повторяется не медианный элемент
    arr01 = [2, 2, 3, 4, 9, 1, 8]
    assert get_median(arr01) == 3
    print('Test #2 OK')

    # повторяется медианный элемент
    arr01 = [2, 6, 6, 4, 9, 1, 6]
    assert get_median(arr01) == 6
    print('Test #3 OK')


if __name__ == '__main__':
    test_median()

    m = 3
    test_array = [random.randint(0, 22) for _ in range(m * 2 + 1)]
    print(test_array)
    median = get_median(test_array)
    print(median)
