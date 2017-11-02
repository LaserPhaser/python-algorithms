# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # write your code here
    segments.sort()
    l = segments[0].end
    point = l
    for s in range(0, len(segments)):
        if segments[s].start > l:
            points.append(point)
            l = segments[s].end
            point = l 
        if segments[s].end < l:
            l = segments[s].end
            point = l
    points.append(point)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # n, *data = map(int,"4 1 1 2 8 3 7 4 5".split())
    # n, *data = map(int,"4 4 7 1 3 2 5 5 6".split())
    # n, *data = map(int,"3 1 3 2 5 3 6".split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
