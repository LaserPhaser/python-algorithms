"""
In computer science, the Rabin–Karp algorithm or Karp–Rabin algorithm is a string searching algorithm
created by Richard M. Karp and Michael O. Rabin (1987)
that uses hashing to find any one of a set of pattern strings in a text.
For text of length n and p patterns of combined length m,

its average and best case running time is O(n+m) in space O(p),
but its worst-case time is O(nm).

"""
import random


def _precompute_hashes(text, pattern_length, prime, x):
    """
    Function for precomputing hashes for text and length of pattern

    Args:
        text: text itself
        pattern_length: length of pattern
        prime: prime number to get modulo of
        x: x random number between 1 and prime

    Returns:
        list of hashes
    """

    hash_list = [0 for _ in range(0, len(text) - pattern_length + 1)]
    S = text[len(text) - pattern_length:len(text)]
    hash_list[len(text) - pattern_length] = _poly_hash(S, prime, x)
    y = 1
    for i in range(1, pattern_length + 1):
        y = (y * x) % prime
    for i in reversed(range(0, len(text) - pattern_length)):
        hash_list[i] = (x * hash_list[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime

    return hash_list


def _poly_hash(text, prime, x):
    """
    Function for generating hash value from text

    Args:
        text: simple text
        prime: prime number to get modulo of
        x: random number between 1 and prime

    Returns:
        hash value of text
    """

    ans = 0
    for c in reversed(text):
        ans = (ans * x + ord(c)) % prime
    return ans


def _find_positions(hash_list, pHash, pattern, text):
    """
    Function for finding position of pattern in text

    Args:
        hash_list: list of hashes from text
        pHash: hash of pattern
        pattern: pattern itself
        text:  text itself

    Returns:
        list of positions where pattern was found

    """

    result = []
    for i in range(0, len(text) - len(pattern) + 1):
        if pHash != hash_list[i]:
            continue
        if text[i:i + len(pattern)] == pattern:  # Only if hashes are the same we compare text symbol by symbol
            result.append(i)
    return result


def rabin_karp(text, pattern):
    """
    Rabin-Karp algorithm that finds all occurrences of pattern in text

    Args:
        text: text to search in
        pattern: pattern to search for

    Returns:
        list of position where pattern placed in text

    Examples:
        >>> rabin_karp('AABAACAADAABAABA', 'AABA')
        [0, 9, 12]

        >>> rabin_karp('aaaaa', 'aaa')
        [0, 1, 2]

    """

    prime = 100000007
    x = random.randint(1, prime)

    pHash = _poly_hash(pattern, prime, x)
    hash_list = _precompute_hashes(text, len(pattern), prime, x)
    return _find_positions(hash_list, pHash, pattern, text)
