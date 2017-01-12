# Uses python3

import sys
import queue


def bfs(adj, Aset):
    # write your code here
    q = queue.Queue()
    for x in Aset:
        q.put(x)
    while not q.empty():
        v = q.get()
        for x in adj[v]:
            if shortest[x] == 1:
                q.put(x)
                shortest[x] = 0
    return 0


def negative_cycle(adj, cost, s):
    # write your code here
    distance[s] = 0
    reachable[s] = 1
    # Bellman Ford Algoritm
    i = 0
    while i < len(adj):
        for u in range(len(adj)):
            if distance[u] == 10 ** 19:
                continue
            for x in range(len(adj[u])):
                v = adj[u][x]
                c = cost[u][x]
                if distance[v] > distance[u] + c:
                    distance[v] = distance[u] + c
                    reachable[v] = 1
                    if i == len(adj) - 1:
                        A.append(v)
        i += 1
    # find cycles with BFS
    bfs(adj, A)

    return 0


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    negative_cycle(adj, cost, s)
    # write your code here
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    dist = [10 ** 19 for _ in range(n)]
    A = []
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    visited = [False] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
