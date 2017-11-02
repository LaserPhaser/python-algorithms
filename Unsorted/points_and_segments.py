import random
import sys


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
    return a


def binary_search(a, x):
    left, right = 0, len(a)
    left = 0
    right = (len(a) - 1)

    while left <= right:
        mid = left + (right - left) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    if (len(ends) > 1):
        ends = randomized_quick_sort(ends, 0, len(ends) - 1)

    if (len(starts) > 1):
        starts = randomized_quick_sort(starts, 0, len(starts) - 1)

    indexes = sorted(range(len(points)), key=lambda x: points[x])
    if (len(points) > 1):
        points = randomized_quick_sort(points, 0, len(points) - 1)
    ll = randomized_quick_sort(starts + ends + points, 0, len(starts + ends + points) - 1)

    point = 0
    s, e, p = 0, 0, 0
    ind = 0
    i = 0
    mp, ms, me = 1, 1, 1
    while i < len(ll) - 1:
        if (len(starts) > s and ll[i] == starts[s]):
            ms = 0
            while len(starts) > s and ll[i] == starts[s]:
                ms += 1
                s += 1

                point += 1
        if (len(points) > p and ll[i] == points[p]):
            mp = 0
            while len(points) > p and ll[i] == points[p]:
                mp += 1
                cnt[indexes[p]] = point

                p += 1
        if (len(ends) > e and ll[i] == ends[e]):
            me = 0
            while len(ends) > e and ll[i] == ends[e]:
                me += 1
                e += 1

                point -= 1

        i += min(ms, mp, me)

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')
