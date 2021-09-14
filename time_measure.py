import timeit


def test_me(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                a = 0


print(timeit.timeit('test_me(2)', number=100, globals=globals()))
print(timeit.timeit('test_me(4)', number=100, globals=globals()))
print(timeit.timeit('test_me(6)', number=100, globals=globals()))
print(timeit.timeit('test_me(10)', number=100, globals=globals()))
