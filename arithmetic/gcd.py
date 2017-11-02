def gcd(a, b):
    if a <=0 or b<=0:
        raise ValueError('GCD is not support negative numbers and zeros')
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd
