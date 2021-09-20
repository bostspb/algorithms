"""
Задача №1
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
- алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
- постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random


def bubble_sort_desc(array):
    j = 0
    while j < len(array):
        for i in range(0, len(array) - j - 1):
            if array[i+1] > array[i]:
                array[i], array[i+1] = array[i+1], array[i]
        j += 1
    return array


if __name__ == '__main__':
    test_array = [random.randint(-100, 99) for _ in range(10)]
    print(test_array)
    bubble_sort_desc(test_array)
    print(test_array)

