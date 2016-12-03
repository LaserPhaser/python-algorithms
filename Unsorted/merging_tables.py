# python3

import sys


class UnionByRank(object):
    def __init__(self, data, n, rank):
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
            self.parent_int[i] = self.find_and_compress(self.parent_int[i])  # Path compression
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


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
# n, m = 6, 4
# lines = [10, 0, 5, 0, 3, 3]
# rank = [1] * n
# parent = list(range(0, n))
ans = max(lines)
union = UnionByRank(data=lines, rank=lines, n=n)


def getParent(table):
    # find parent and compress path
    return union.find(table)
    # return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False
    union.union(realSource, realDestination)
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    return True


# xx = [[3, 5], [2, 4], [1, 4], [5, 4], [5, 3]]x
# xx = [[6, 6], [6, 5], [5, 4], [4, 3]]
# xx = [[5, 3], [2, 4], [1, 4]]
# xx = [[2, 4], [5, 2], [3,1],[2, 3], [2, 6]]
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    # destination, source = xx[i][0], xx[i][1]
    merge(destination - 1, source - 1)
    print(union.maxdata)
