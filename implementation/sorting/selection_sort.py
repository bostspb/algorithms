"""
Сортировка выбором / Selection Sort

1) находим номер минимального значения в текущем списке
2) производим обмен этого значения со значением первой неотсортированной позиции (обмен не нужен,
   если минимальный элемент уже находится на данной позиции)
3) теперь сортируем хвост списка, исключив из рассмотрения уже отсортированные элементы

Сложность алгоритма O(N^2), где N - количество элементов.
Неустойчивая сортировка.
"""


def selection_sort(arr):
    for i in range(len(arr)):
        idx_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[idx_min], arr[i] = arr[i], arr[idx_min]
        print(arr)


array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]
selection_sort(array)
print(array)



#########
def select_sort(a):
    for i in range(len(a)-1):
        for k in range(i+1, len(a)):
            if a[k] < a[i]:
                a[k], a[i] = a[i], a[k]