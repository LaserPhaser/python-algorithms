"""
Calculating (n-th Fibonacci number) mod m
"""


def _fib(number):
    """
    Fibonacci number

    Args:
        number: number of sequence

    Returns:
        array of numbers
    """

    init_array = [0, 1]
    for idx in range(2, number + 1):
        init_array.append(init_array[idx - 1] + init_array[idx - 2])
    return init_array[number]


def _pisano_period_len(modulo):
    """
    In number theory, the nth Pisano period, written π(n),
    is the period with which the sequence of Fibonacci numbers taken modulo n repeats.

    Args:
        modulo: modulo

    Returns:
        length of Pisano period
    """
    init_array = [0, 1]
    idx = 1
    while 1:
        idx += 1
        init_array.append(init_array[idx - 1] % modulo + init_array[idx - 2] % modulo)
        if init_array[idx] % modulo == 1 and init_array[idx - 1] % modulo == 0:
            return len(init_array) - 2


def fibonacci_modulo(number, modulo):
    """
    Calculating (n-th Fibonacci number) mod m

    Args:
        number: fibonacci number
        modulo: modulo

    Returns:
        (n-th Fibonacci number) mod m

    Examples:
        >>> fibonacci_modulo(11527523930876953, 26673)
        10552
    """

    period = _pisano_period_len(modulo)
    answer = _fib(number - number // period * period) % modulo
    return answer
