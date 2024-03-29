"""
Сортировка слиянием / Merge sort

1. Сортируемый массив разбивается на две части примерно одинакового размера;
2. Каждая из получившихся частей сортируется отдельно тем же самым алгоритмом;
3. Два упорядоченных массива половинного размера соединяются в один.
    3.1. На каждом шаге мы берём меньший из двух первых элементов подмассивов и записываем его в результирующий массив.
         Счётчики номеров элементов результирующего массива и подмассива, из которого был взят элемент, увеличиваем на 1.
    3.2. «Прицепление» остатка: rогда один из подмассивов закончился,
         мы добавляем все оставшиеся элементы второго подмассива в результирующий массив.

Сложность алгоритма O(n log n), где n - количество элементов.
Устойчивая сортировка.
"""


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