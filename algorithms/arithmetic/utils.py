"""
Module that contain extra checkers
"""


def positive_integer(number) -> None:
    """
    Function that check that value is integer and greater than 0,
    Raise exception if it's not.
    """
    if not isinstance(number, int):
        raise TypeError('Number is not integer type')
    if number <= 0:
        raise ValueError('Number is not positive')
