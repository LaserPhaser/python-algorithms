def merge(a, b):
    d = []
    sk = len(a)
    i, j, inv = 0, 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            d += [a[i]]
            i += 1
            sk -= 1
        else:
            inv += sk
            d += [b[j]]
            j += 1
    d += a[i:len(a)]
    d += b[j:len(b)]

    return inv, d


def merge_sort(a):
    j = 0
    if len(a) == 1:
        return j, a[:]
    ave = len(a) // 2
    j1, b = merge_sort(a[:ave])
    j2, c = merge_sort(a[ave:])
    j = j1 + j2
    j3, a2 = merge(b, c)
    j += j3

    return j, a2
