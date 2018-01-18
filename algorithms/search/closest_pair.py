"""
The closest pair of points problem or closest pair problem is a problem of computational geometry:
given n points in metric space, find a pair of points with the smallest distance between them.
The closest pair problem for points in the Euclidean plane[1] was among the first geometric problems that
were treated at the origins of the systematic study of the computational complexity of geometric algorithms. [Wikipedia]
"""

import math


def _distance(point1, point2):
    """
    Function for calculation distance between 2 points

    Args:
        point1: first point with coordinates as tuple (x, y)
        point2: first point with coordinates as tuple (x, y)

    Returns:
        Distance between 2 points

    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def brute_force_distance(points):
    """
    Brute force solution for closest pair problem

    Complexity: O(n^2)

    Args:
        points: list of points in the following format [(x1, y1), (x2, y2), ... , (xn, yn)]

    Returns:
        Minimum distance between points

    Examples:
        >>> n_log_n_squared_distance([(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)])
        1.4142135623730951

    """
    if len(points) == 1:
        return 0
    # Calculating distance between first two points
    min_d = _distance(points[0], points[1])
    for x1 in range(len(points)):
        for x2 in range(len(points)):
            distance = _distance(points[x1], points[x2])
            if (x1 != x2) and distance < min_d:
                min_d = distance
    return min_d


def n_log_n_squared_distance(points):
    """
    O(N (LogN)^2) solution for closest pair problem

    Complexity: O(n (log n)^2)

    Args:
        points: list of points in the following format [(x1, y1), (x2, y2), ... , (xn, yn)]

    Returns:
        Minimum distance between points

    Examples:
        >>> n_log_n_squared_distance([(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)])
        1.4142135623730951
    """
    # Points have to be sorted by x coordinate
    points = sorted(points, key=lambda x: x[0])
    return _n_log_n_squared_distance(points)


def _n_log_n_squared_distance(points):
    """
    O(N (LogN)^2) solution for closest pair problem

    Complexity: O(n (log n)^2)

    Args:
        points: list of points in the following format [(x1, y1), (x2, y2), ... , (xn, yn)]

    Returns:
        Minimum distance between points
    """

    if len(points) == 1:
        return 0
    if len(points) <= 3:
        return brute_force_distance(points)
    # splitting points to the 2 parts

    mid = len(points) // 2

    min_d1 = n_log_n_squared_distance(points[:mid])
    min_d2 = n_log_n_squared_distance(points[mid:])
    min_d = min(min_d1, min_d2)

    strip = []

    # Adding point to the strip array if the distance between point and the "vertical" line that we split
    # is less than minimum distance that we have find.
    for point in points:
        x = point[0]
        if abs(x - points[mid][0]) < min_d:
            strip.append(point)

    return min(min_d, _closest_split_pair(strip, min_d))


def _closest_split_pair(points, delta):
    """
        Function for check boundaries points (points that close to the split line than minimum delta)

    Args:
        points: list of points in the following format [(x1, y1), (x2, y2), ... , (xn, yn)]
        delta: delta (minimum distance)

    Returns:
        minimum distance between points
    """

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if (points[j][1] - points[i][1]) < delta and _distance(points[i], points[j]) < delta:
                delta = _distance(points[i], points[j])
    return delta
