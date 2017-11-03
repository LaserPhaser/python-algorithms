"""
The least common multiple, lowest common multiple, or smallest common multiple of two integers a and b,
usually denoted by LCM(a, b), is the smallest positive integer that is divisible by both a and b. [Wikipedia]
"""
from functools import reduce

from arithmetic.gcd import gcd


def _lcm(integer_a: int, integer_b: int) -> int:
    _gcd = gcd(integer_a, integer_b)  # Move here to have extra check that we have in GCD
    return int(abs(integer_a * integer_b) / _gcd)


def lcm(*integer_nums: int) -> int:
    return int(reduce((lambda i, j: _lcm(i, j)), integer_nums))
