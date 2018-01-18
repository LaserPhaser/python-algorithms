"""
In computer science, binary search is a search algorithm that finds the position of a target value within
a sorted array. Binary search compares the target value to the middle element of the array; if they are unequal,
the half in which the target cannot lie is eliminated and the search continues on the remaining half
until it is successful. If the search ends with the remaining half being empty, the target is not in the array.
"""


def binary_search(sorted_array, target_element):
    """
    Binary search algorithm

    Args:
        sorted_array: list of sorted elements (integers)
        target_element:  element to find

    Returns:
        position of target_element if succes
        -1 if element is not found

    Examples:
        >>> binary_search([1, 2, 3, 4], 5)
        -1


        >>> binary_search([x for x in range(10000)], 26)
        26

    """

    left = 0
    right = (len(sorted_array) - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if target_element == sorted_array[mid]:
            return mid
        elif target_element < sorted_array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
