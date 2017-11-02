# Uses python3


import sys
import queue


class BiDij:

    def __init__(self, n):
        self.n = n  # Number of nodes
        self.inf = n * 10 ** 6  # All distances in the graph are smaller
        self.d = [[self.inf] * n, [self.inf] * n]  # Initialize distances for forward and backward searches
        self.visited = [False] * n  # visited[v] == True iff v was visited by forward or backward search
        self.visits = [[False] * n, [False] * n]
        self.workset = []  # All the nodes visited by forward or backward search
        self.dist = []

    def clear(self):
        """
        Reinitialize the data structures for the next query after the previous query.
        """
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visits[1][v] = self.visits[0][v] = False
        del self.workset[0:len(self.workset)]

    def visit(self, q, side, v, dist):
        """
        Try to  relax the distance to node v from direction side by value dist.
        """
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            q[side].put((dist, v))
            self.workset.append(v)

    def query(self, adj, cost, s, t):
        """
        Implementaion of bidirectional Dijksta algorithm
        """
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
                # Implement the rest of the algorithm yourself
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
