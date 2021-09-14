import cProfile


def my_len(arr):
    return len(arr)


def my_sum(arr):
    s = 0
    for item in arr:
        s += item
    return s


def main():
    array = [i for i in range(10000000)]
    len_ = my_len(array)
    sum_ = my_sum(array)


cProfile.run('main()')