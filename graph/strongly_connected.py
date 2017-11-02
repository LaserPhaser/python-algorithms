import sys

sys.setrecursionlimit(200000)


def explore(i):
    t[i] = True
    previsit(i)
    for z in adj[i]:
        if reached[z] is False and t[z] is False:
            explore(z)
    reached[i] = True
    t[i] = False
    postvisit(i)
    ids.append(i)
    return 0


def previsit(v):
    global clock
    pre[v] = clock
    clock += 1


def flush_reached():
    global reached
    reached = [False for _ in range(n)]


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


def reverse_adj(adj):
    rev_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for x in adj[i]:
            if x is not None:
                rev_adj[x].append(i)
    return rev_adj


def set_adj(rev_adj):
    global adj
    adj = rev_adj


def number_of_strongly_connected_components(adj):
    scc = 0
    rev_adj = reverse_adj(adj)
    order = []
    DFS(rev_adj)
    flush_reached()
    for i in ids[::-1]:
        order.append(i)
    set_adj(rev_adj)
    for v in order:
        if reached[v] is False:
            explore(v)
            scc += 1

    return scc


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    reached = [False for _ in range(n)]
    post = [False for _ in range(n)]
    pre = [False for _ in range(n)]
    t = [False for _ in range(n)]
    ids = []
    clock = 0

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
