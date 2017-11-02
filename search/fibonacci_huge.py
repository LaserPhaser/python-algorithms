def fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def get_pisano_period_len(m):
    f = [0, 1]
    i = 1
    while 1:
        i += 1
        f.append(f[i - 1] % m + f[i - 2] % m)
        if f[i] % m == 1 and f[i - 1] % m == 0:
            return len(f) - 2
    return len(f)


def get_fibonacci_huge(n, m):
    period = get_pisano_period_len(m)
    answer = fib(n - n // period * period) % m
    return answer
