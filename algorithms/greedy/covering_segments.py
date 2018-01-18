"""
Given a set of n segments {[a(0) ,b(0) ],[a(1) ,b(1) ],…,[a(n)−1 ,b(n)−1 ]} with integer coordinates on a line,
find the minimum number m of points such that each segment contains at least one point.
"""
from collections import namedtuple


def covering_segments(segments: [tuple]) -> list:
    """
    Function for finding minimum number of points that each segment contains

    Args:
        segments: list of tuples with start and end point coordinates

    Returns:
        list of points where segments are crossing

    Examples:
        >>> covering_segments([(4, 7), (1, 3), (2, 5), (5, 6)])
        [3, 6]

    """

    segment = namedtuple('Segment', 'start end')
    points = []
    named_segments = list(map(lambda i: segment(i[0], i[1]), segments))
    named_segments.sort()
    end_point = named_segments[0].end
    point = end_point
    for segment_index in range(0, len(named_segments)):
        if named_segments[segment_index].start > end_point:
            points.append(point)
            end_point = named_segments[segment_index].end
            point = end_point
        if named_segments[segment_index].end < end_point:
            end_point = named_segments[segment_index].end
            point = end_point
    points.append(point)
    return points
