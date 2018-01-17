import queue
import sys


def relax(u, v):
    pass


def distance(adj, cost, s, t):
    dist[s] = 0
    q = queue.PriorityQueue()
    for x in range(n):
        q.put(x, dist[x])
    while not q.empty():
        u = q.get()
        for x in range(len(adj[u])):
            if dist[u] + cost[u][x] < dist[adj[u][x]]:
                dist[adj[u][x]] = dist[u] + cost[u][x]
                q.put(adj[u][x], dist[adj[u][x]])
    if dist[t] == 10 ** 19:
        return -1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0: 2]
    data = data[2:]
    edges = list(zip(zip(data[0: (3 * m): 3], data[1: (3 * m): 3]), data[2: (3 * m): 3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    dist = [10 ** 19 for _ in range(n)]

    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
