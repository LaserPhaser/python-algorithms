"""
The least common multiple, lowest common multiple, or smallest common multiple of two integers a and b,
usually denoted by LCM(a, b), is the smallest positive integer that is divisible by both a and b. [Wikipedia]
"""
from functools import reduce

from algorithms.arithmetic.gcd import gcd


def _lcm(integer_a: int, integer_b: int) -> int:
    """
    Private function for calculating LCM [least common multiple] of 2 integers

    Args:
        integer_a: first integer
        integer_b: second integer

    Returns:
        Least common multiple of 2 positive integers.
    """

    # Move here to have extra check that we have in GCD
    _gcd = gcd(integer_a, integer_b)

    return int(abs(integer_a * integer_b) / _gcd)


def lcm(*integer_nums: int) -> int:
    """
    Private function for calculating LCM [least common multiple] of N integers

    Args:
        *integer_nums: list of integers

    Returns:
        Least common multiple of N positive integers.
    """

    return int(reduce((lambda i, j: _lcm(i, j)), integer_nums))
