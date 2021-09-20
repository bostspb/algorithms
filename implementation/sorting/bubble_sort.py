"""
Сортировка пузырьком / Bubble Sort

Перебираем элементы и на каждой итерации сравниваем два соседних элемента.
Если слева элемент больше - меняем их местами.
В результате самый большой, который попался, окажется в конце списка.
Необходимо совершить N проходов для окончания сортировки, где N - количество элементов.

Сложность алгоритма O(N^2), где N - количество элементов.
Устойчивая сортировка.
"""
array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]

n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)

print(array)