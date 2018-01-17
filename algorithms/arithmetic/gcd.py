"""
Greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest positive integer that
divides each of the integers.
"""
from functools import reduce

from algorithms.arithmetic.utils import positive_integer


def _gcd(integer_a: int, integer_b: int) -> int:
    """
    Private function for calculating GCD [greatest common divisor] of 2 integers

    Args:
        integer_a: first integer
        integer_b: second integer

    Returns:
        Greatest common divisor of 2 positive integers.
    """
    # Check that numbers are positive integers
    positive_integer(integer_a)
    positive_integer(integer_b)

    current_gcd = 1
    for divisor in range(2, min(integer_a, integer_b) + 1):
        if integer_a % divisor == 0 and integer_b % divisor == 0:
            if divisor > current_gcd:
                current_gcd = divisor
    return current_gcd


def gcd(*integer_nums: int) -> int:
    """
    Function for calculating GCD [greatest common divisor] of N integers

    Args:
        *integer_nums: integer arguments

    Returns:
        Greatest common divisor of N positive integers

    Examples:
        >>> gcd(54, 24)
        6

        >>> gcd(2, 4, 6, 8, 16)
        2
    """

    return int(reduce((lambda i, j: _gcd(i, j)), integer_nums))
