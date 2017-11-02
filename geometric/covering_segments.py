import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []

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

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
