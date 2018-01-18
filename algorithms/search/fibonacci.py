"""
In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence,
and characterized by the fact that every number after the first two is the sum of the two preceding ones:
"""


def fibonacci(number):
    """
    Recursive implementation of fibonacci function

    Args:
        number: number in fibonacci sequence

    Returns:
        fibonacci number

    Examples:
        >>> fibonacci_recursive(20)
        6765
    """

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)
