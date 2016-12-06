# python3
import random


def precompute_hashes(text, pattern_length, prime, x):
    H = [0 for i in range(0, len(text) - pattern_length + 1)]
    S = text[len(text) - pattern_length:len(text)]
    H[len(text) - pattern_length] = poly_hash(S, prime, x)
    y = 1
    for i in range(1, pattern_length + 1):
        y = (y * x) % prime
    for i in reversed(range(0, len(text) - pattern_length)):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime

    return H


def poly_hash(S, prime, x):
    ans = 0
    for c in reversed(S):
        ans = (ans * x + ord(c)) % prime
    return ans


def rabin_karp(text, pattern):
    prime = 100000007
    x = random.randint(1, prime)
    result = []
    pHash = poly_hash(pattern, prime, x)
    H = precompute_hashes(text, len(pattern), prime, x)
    for i in range(0, len(text) - len(pattern) + 1):
        if pHash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


def get_occurrences(pattern, text):
    return rabin_karp(text, pattern)

