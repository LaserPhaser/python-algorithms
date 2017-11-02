# Uses python3

import sys


def negative_cycle(adj, cost):
    # write your code here
    dist[0] = 0
    # Bellman Ford Algoritm
    for _ in range(n):
        for u in range(len(adj)):
            for x in range(len(adj[u])):
                if dist[u] + cost[u][x] < dist[adj[u][x]]:
                    dist[adj[u][x]] = dist[u] + cost[u][x]
    # Check for negative cycle
    for u in range(len(adj)):
        for x in range(len(adj[u])):
            if dist[u] + cost[u][x] < dist[adj[u][x]]:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    dist = [10**19 for _ in range(n)]

    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
