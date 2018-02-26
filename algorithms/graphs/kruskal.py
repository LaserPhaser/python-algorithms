"""
Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that
connects any two trees in the forest.[Wikipedia]
"""
import heapq
import math
import sys


class UnionByRank(object):
    def __init__(self, data, n):
        self.data = data
        self.parent_int = list(range(0, n))
        self.symlink = list(range(0, n))
        self.rank = [1] * (len(self.parent_int))
        self.maxdata = max(self.data)

    def find(self, i):
        while i != self.parent_int[i]:
            i = self.parent_int[i]
        return i

    def find_and_compress(self, i):
        if i != self.parent_int[i]:
            self.parent_int[i] = self.find_and_compress(self.parent_int[i])
        return self.parent_int[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent_int[j_id] = i_id
            self.data[self.symlink[i_id]] += self.data[self.symlink[j_id]]
            if self.data[self.symlink[i_id]] > self.maxdata:
                self.maxdata = self.data[self.symlink[i_id]]
            self.symlink[j_id] = i_id

        else:
            self.parent_int[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
            self.data[self.symlink[j_id]] += self.data[self.symlink[i_id]]
            if self.data[self.symlink[j_id]] > self.maxdata:
                self.maxdata = self.data[self.symlink[j_id]]
            self.symlink[i_id] = j_id


def minimum_distance(x, y):
    result = 0
    union = UnionByRank(data=[z for z in range(n)], n=n)
    weight = []

    for v in range(len(x)):
        for c in range(v + 1, len(x)):
            if c != v:
                heapq.heappush(weight, (math.sqrt((x[v] - x[c]) ** 2 + (y[v] - y[c]) ** 2), v, c))

    while weight:

        distance, x, y = heapq.heappop(weight)
        if union.find(x) != union.find(y):
            result += distance
            union.union(x, y)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
