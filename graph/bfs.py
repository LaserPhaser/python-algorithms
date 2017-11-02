# Uses python3

import sys
import queue


# def bfs(adj, s):


def distance(adj, s, t):
    # write your code here
    q = queue.Queue()
    layer[s] = 0
    visited[s] = True
    q.put(s)
    while not q.empty():
        v = q.get()
        for x in adj[v]:
            if visited[x] is False:
                visited[x] = True
                layer[x] = layer[v] + 1
                q.put(x)
    if layer[t] > n:
        return -1
    return layer[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    layer = [n + 1 for _ in range(n)]
    visited = [False for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
