import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = left + (right - left) // 2
    ret1 = get_majority_element(a[left:mid], 0, mid)
    ret2 = get_majority_element(a[mid:right + 1], 0, mid)
    if ret1 == ret2:
        return ret1
    check1 = 0
    check2 = 0
    for i in range(len(a)):
        if a[i] == ret1:
            check1 += 1
        if a[i] == ret2:
            check2 += 1
    if (check1 > mid):
        return ret1
    if (check2 > mid):
        return ret2
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
