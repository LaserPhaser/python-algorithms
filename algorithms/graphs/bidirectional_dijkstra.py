import queue
import sys


class BiDij:
    def __init__(self, n):
        self.n = n
        self.inf = n * 10 ** 6
        self.d = [[self.inf] * n, [self.inf] * n]
        self.visited = [False] * n
        self.visits = [[False] * n, [False] * n]
        self.workset = []
        self.dist = []

    def clear(self):

        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visits[1][v] = self.visits[0][v] = False
        del self.workset[0:len(self.workset)]

    def visit(self, q, side, v, dist):

        if self.d[side][v] > dist:
            self.d[side][v] = dist
            q[side].put((dist, v))
            self.workset.append(v)

    def query(self, adj, cost, s, t):

        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)
        proc = [[], []]
        flip_side = 0
        while not q[0].empty() or not q[1].empty():
            v = q[flip_side].get()[1]
            for x in range(len(adj[flip_side][v])):
                dist = self.d[flip_side][v] + cost[flip_side][v][x]
                self.visit(q, flip_side, adj[flip_side][v][x], dist)
            proc[flip_side].append(v)
            self.visits[flip_side][v] = True
            if self.visits[flip_side ^ 1][v] is True:
                return self.ShortestPath(proc)
            if not q[flip_side ^ 1].empty():
                flip_side ^= 1

        return -1

    def ShortestPath(self, proc):
        distance = 10 ** 16
        for u in proc[1] + proc[0]:
            if self.d[0][u] + self.d[1][u] < distance:
                distance = self.d[0][u] + self.d[1][u]
        return distance


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s - 1, t - 1))
