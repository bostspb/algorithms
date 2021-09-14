import cProfile
import timeit

# Вариант №1. Рекурсия
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Вариант №2. Рекурсия + меморизация
def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]
    return _fib_dict(n)


# Вариант №3. Цикл
def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


def test_fib(func):
    test_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, item in enumerate(test_array):
        assert item == func(i)
        print(f'Test {i} OK')


def print_time(f_name):
    print(timeit.timeit(f_name + '(5)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(10)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(15)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(20)', number=100, globals=globals()))
    print(timeit.timeit(f_name + '(25)', number=100, globals=globals()))


def print_profile(f_name):
    cProfile.run(f_name + '(5)')
    cProfile.run(f_name + '(10)')
    cProfile.run(f_name + '(15)')
    cProfile.run(f_name + '(20)')
    cProfile.run(f_name + '(25)')

#test_fib(fib)
#print_time('fib')
#print_profile('fib')

#test_fib(fib_dict)
#print_time('fib_dict')
#print_profile('fib_dict')

#test_fib(fib_loop)
#print_time('fib_loop')
print_profile('fib_loop')
