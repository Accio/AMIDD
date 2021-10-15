#!/usr/bin/env python3

def recursive_fib(n: int):
    """A recursive version of Fibonacci"""
    if (n<=1):
        return n;
    return recursive_fib(n-1) + recursive_fib(n-2)

def dp_fib(n: int):
    """A dynamic programming version of Fibonacci"""
    res = [0, 1]
    for i in range(2, n+1):
        res.append(res[i-1] + res[i-2])
    return res[n]

if __name__ == '__main__':
    import timeit

    print("Recursive fib(25):%d" % recursive_fib(25))
    print(timeit.timeit("recursive_fib(25)", number=100, globals=locals()))

    print("Dynamic Programming fib(25):%d" % dp_fib(25))
    print(timeit.timeit("dp_fib(25)", number=100, globals=locals()))
