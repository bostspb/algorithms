#сортировка Тони Хоара, быстрая сортировка

#бинарный поиск в отсортированном массиве
#O(log2 N)

#Динамическое программирование
#фибаначевое дерево



#Слияние
def merge(A:list, B:list):
    C = [0] * (len(A) + len(B))
    i=k=n=0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

# сортировка слиянием
def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    A = C[:]


SS = [1, 5, 9, 5, 9, 7, 5, 7, 2, 1, 99, 45, 5, 6, 78]
merge_sort(SS)
print(SS)
