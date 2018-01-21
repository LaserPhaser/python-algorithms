"""
Quicksort (sometimes called partition-exchange sort) is an efficient sorting algorithm,
serving as a systematic method for placing the elements of an array in order.
Developed by Tony Hoare in 1959[1] and published in 1961,[2] it is still a commonly used algorithm for sorting. [Wikipedia]

https://en.wikipedia.org/wiki/Quicksort

Average complexity: O(n log n)
Worst case:  O(n^2)
"""
import random


def _partition(array, low, high):
    """
    Function that sorts elements,
    swaps to elements with the following logic:
    we take the pivot element and trying to find left to right elements that are greater than pivot
    then we trying to find element from right to left that are less that pivot , and then we swaps them


    """
    pivot = array[low]
    mid = low
    i = low

    while i <= high:
        if array[i] < pivot:
            array[i], array[mid] = array[mid], array[i]
            mid += 1
        elif array[i] > pivot:
            array[i], array[high] = array[high], array[i]
            high -= 1
        else:
            i += 1
    return mid, high


def quick_sort(array, low, high):
    """
    Quick Sort function sorts array

    Args:
        array: list of elements
        low: at starting point low must be  = 0
        high: at starting point high must be = len(array)-1

    Returns:
        list: sorted array

    Examples:
        >>> quick_sort([4,  9,  4,  4,  1,  9,  4,  4,  9,  4,  4,  1,  4], 0, 12)
        [1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 9, 9, 9]

        >>> quick_sort([1, 10, 32, 4.], 0, 3)
        [1, 4.0, 10, 32]
    """
    if low >= high:
        return

    pivot = random.randint(low, high)

    array[low], array[pivot] = array[pivot], array[low]
    m1, m2 = _partition(array, low, high)
    quick_sort(array, low, m1 - 1)
    quick_sort(array, m2 + 1, high)
    return array
