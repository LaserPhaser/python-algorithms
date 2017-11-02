"""
Greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest positive integer that
divides each of the integers.
"""


def gcd(integer_a: int, integer_b: int) -> int:
    """
    Function for calculating GCD [greatest common divisor] of 2 integers
    :return: greatest common divisor of 2 integers
    """
    value_check(integer_a, integer_b)

    current_gcd = 1
    for divisor in range(2, min(integer_a, integer_b) + 1):
        if integer_a % divisor == 0 and integer_b % divisor == 0:
            if divisor > current_gcd:
                current_gcd = divisor
    return current_gcd


def value_check(integer_a, integer_b) -> None:
    """
    Function that check that both values are integers and greater than 0,
    Raise exception if it's not.
    """
    if integer_a <= 0 or integer_b <= 0:
        raise ValueError('GCD is not support negative numbers and zeros')
    if not isinstance(integer_a, int) or not isinstance(integer_b, int):
        raise TypeError('GCD function support only integer types')
