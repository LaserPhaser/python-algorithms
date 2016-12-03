def lcm(a, b):
    tmp_a = a
    while (tmp_a % b) != 0:
        tmp_a += a
    return a * b
