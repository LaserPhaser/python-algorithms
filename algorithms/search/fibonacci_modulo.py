"""
Calculating (n-th Fibonacci number) mod m
"""


def _fib(number):
    """
    fibonacci number
    :param number: number of sequence
    :return: array of numbers
    """
    init_array = [0, 1]
    for idx in range(2, number + 1):
        init_array.append(init_array[idx - 1] + init_array[idx - 2])
    return init_array[number]


def _pisano_period_len(modulo):
    """
    In number theory, the nth Pisano period, written π(n),
    is the period with which the sequence of Fibonacci numbers taken modulo n repeats.
    :param modulo:
    :return: length of pisano period
    """
    init_array = [0, 1]
    idx = 1
    while 1:
        idx += 1
        init_array.append(init_array[idx - 1] % modulo + init_array[idx - 2] % modulo)
        if init_array[idx] % modulo == 1 and init_array[idx - 1] % modulo == 0:
            return len(init_array) - 2


def fibonacci_modulo(n, m):
    """
    Calculating (n-th Fibonacci number) mod m
    :param n: fibonacci number
    :param m: modulo
    :return: (n-th Fibonacci number) mod m
    """
    period = _pisano_period_len(m)
    answer = _fib(n - n // period * period) % m
    return answer
