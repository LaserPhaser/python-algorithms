import random


def partition3(a, l, r):
    x = a[l]
    j = l
    i = l
    k = r
    while i <= k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
        else:
            i += 1
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
