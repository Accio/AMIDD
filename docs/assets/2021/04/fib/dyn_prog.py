#!/usr/bin/env python3

def recursive_fib(n: int):
    """A recursive version of Fibonacci"""
    if n <= 1:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)


def dp_fib_ls(n: int):
    """A dynamic programming version of Fibonacci, linear space"""
    res = [0, 1]
    for i in range(2, n+1):
        res.append(res[i-2] + res[i-1])

    return res[n]


def dp_fib_cs(n: int):
    """A dynamic programming version of Fibonacci, constant space"""
    a = 1  # f(n-2)
    b = 1  # f(n-1)

    for i in range(2, n):
        a, b = b, a + b

    return b


if __name__ == '__main__':
    import timeit

    print("Recursive fib(25):%d" % recursive_fib(25))
    print(timeit.timeit("recursive_fib(25)", number=100, globals=locals()))

    print("Dynamic Programming, linear space fib(25):%d" % dp_fib_ls(25))
    print(timeit.timeit("dp_fib_ls(25)", number=100, globals=locals()))

    print("Dynamic Programming, constant space fib(25):%d" % dp_fib_cs(25))
    print(timeit.timeit("dp_fib_cs(25)", number=100, globals=locals()))
