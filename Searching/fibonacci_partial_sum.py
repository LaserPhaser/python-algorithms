# Uses python3
import sys


def get_pisano_period_len(m):
    f = []
    f.append(0)
    f.append(1)
    i = 2
    while 1:
        f.append(f[i - 1] % m + f[i - 2] % m)
        if f[i] % m == 1 and f[i - 1] % m == 0:
            return (len(f) - 2)
        i += 1
    return (len(f))


def fib_sum(n):
    f = []
    if n == 0:
        return 0
    s = 1
    f.append(0)
    f.append(1)
    for i in range(2, n + 1):
        f.append(f[i - 1] % 10 + f[i - 2] % 10)
        s += f[i]
    return (s)


def get_fibonacci_partial_sum(from_, to):
    m = 10
    period = get_pisano_period_len(m)
    from_ -= 1
    answer = fib_sum(from_ - from_ // period * period)
    answer = fib_sum(to - to // period * period) - answer
    return answer % m
