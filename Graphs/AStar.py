#!/usr/bin/python3

import sys
import queue
import math




class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n * 10 ** 6
        self.d = [self.inf] * n
        self.visited = [False] * n
        self.workset = []
        # Coordinates of the nodes
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False
        del self.workset[0:len(self.workset)]

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, v, dist, measure):
        # Implement this method yourself
        if self.d[v] > dist:
            self.d[v] = dist

            q.put((dist + measure, v))

            self.workset.append(v)

    def potential(self, v, t):
        return math.sqrt((self.x[v] - self.x[t]) ** 2 + (self.y[v] - self.y[t]) ** 2)

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        q = queue.PriorityQueue()
        self.visit(q, s, 0, self.potential(s, t))
        while not q.empty():
            v = q.get()[1]
            if v == t:
                return self.d[t]
            if self.visited[v]:
                continue
            for x in range(len(self.adj[v])):
                dist = self.d[v] + self.cost[v][x]
                poten = self.potential(adj[v][x], t)
                self.visit(q, adj[v][x], dist, poten)

            self.visited[v] = True

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = readl()
        adj[u - 1].append(v - 1)
        cost[u - 1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s - 1, t - 1))
