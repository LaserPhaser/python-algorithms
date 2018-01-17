"""
Helper functions for arithmetic namespace
"""


def positive_integer(number) -> None:
    """
    Function that check that value is integer and greater than 0

    Args:
        number: Any number

    Raises:
        TypeError: if `number` is not int type
        ValueError  if `number` <= 0
    """

    if not isinstance(number, int):
        raise TypeError('Number is not integer type')
    if number <= 0:
        raise ValueError('Number is not positive')
