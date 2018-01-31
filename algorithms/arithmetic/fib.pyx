cpdef long long fib_fast(long long n):
    if n <= 1:
        return n

    return fib_fast(n - 1) + fib_fast(n - 2)

