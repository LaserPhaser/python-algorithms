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


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))

ans = max(lines)
union = UnionByRank(data=lines, rank=lines, n=n)


def getParent(table):
    return union.find(table)


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False
    union.union(realSource, realDestination)

    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())

    merge(destination - 1, source - 1)
    print(union.maxdata)
