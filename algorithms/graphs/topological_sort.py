import sys


def explore(i):
    if t[i]:
        return 1
    t[i] = True
    previsit(i)
    for z in adj[i]:
        if reached[z] is False:
            if explore(z) == 1:
                return 1
    reached[i] = True
    t[i] = False
    postvisit(i)
    ids.append(i)
    return 0


def previsit(v):
    global clock
    pre[v] = clock
    clock += 1


def postvisit(v):
    global clock
    post[v] = clock
    clock += 1


def DFS(adj):
    n = len(adj)
    for i in range(n):
        if not reached[i]:
            explore(i)
    return 0


def dfs(adj, used, order, x):
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    DFS(adj)
    for i in ids[::-1]:
        order.append(i)

    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    reached = [False for _ in range(n)]
    post = [False for _ in range(n)]
    pre = [False for _ in range(n)]
    t = [False for _ in range(n)]
    ids = []
    clock = 0
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
