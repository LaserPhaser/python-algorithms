"""
The least common multiple, lowest common multiple, or smallest common multiple of two integers a and b,
usually denoted by LCM(a, b), is the smallest positive integer that is divisible by both a and b. [Wikipedia]
"""


def lcm(a, b):
    tmp_a = a
    while (tmp_a % b) != 0:
        tmp_a += a
    return a * b
