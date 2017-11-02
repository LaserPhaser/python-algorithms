import sys


def explore(i):
    if t[i]:
        return 1
    t[i] = True
    for z in adj[i]:
        if reached[z] is False:
            if explore(z) == 1:
                return 1
    reached[i] = True
    t[i] = False
    return 0


def DFS(adj):
    n = len(adj)
    for i in range(n):
        if not reached[i]:
            if explore(i) == 1:
                return 1
    return 0


def acyclic(adj):
    return DFS(adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]

    reached = [False for _ in range(n)]
    t = [False for _ in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
