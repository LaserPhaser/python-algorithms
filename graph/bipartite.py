import queue
import sys


def bipartite(adj):
    q = queue.Queue()
    s = 0
    color[s] = 1
    visited[s] = True
    q.put(s)
    while not q.empty():
        v = q.get()
        for x in adj[v]:
            if visited[x] is True and color[x] == color[v]:
                return 0
            if visited[x] is False:
                visited[x] = True
                color[x] = color[v] * -1
                q.put(x)
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    color = [2 for _ in range(n)]
    visited = [False for _ in range(n)]

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
