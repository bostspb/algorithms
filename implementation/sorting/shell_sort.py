"""
Сортировка Шелла / Shell sort

Усовершенствованный вариант сортировки вставками.
Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом,
но и на определённом расстоянии друг от друга.
Иными словами — это сортировка вставками с предварительными «грубыми» проходами.

Сложность алгоритма O(n^5/4) вроде как, в википедии O(n^2), где n - количество элементов.
В среднем O(n log2 n)
Устойчивая сортировка?
"""


def shell_sort_w(data):
    last_index = len(data) - 1
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data


def shell_sort(arr):
    assert len(arr) < 4000, 'Массив слишком большой'

    def new_increment(arr):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(arr) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(arr):
        for i in range(increment, len(arr)):
            for j in range(i, increment - 1, -increment):
                if arr[j - increment] <= arr[j]:
                    break
                arr[j], arr[j - increment] = arr[j - increment], arr[j]
        print(arr)


array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]
print(array)
shell_sort(array)
print(array)
