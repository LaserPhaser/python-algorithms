"""
The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all
of the other vertices in a weighted digraph.
It is slower than Dijkstra's algorithm for the same problem, but more versatile,
as it is capable of handling graphs in which some of the edge weights are negative numbers. [Wikipedia]
"""
from algorithms.graphs import num_of_nodes


def negative_cycle(graph, start_node):
    """
    Bellman-Ford algorithm for negative cycle detection

    Args:
        graph: graph itself

    Returns:
        bool: True if negative cycle detected, False otherwise

    Examples:
        >>> negative_cycle({0: {1: 1}, 1: {2: -1}, 2: {3: -1}, 3: {0: -1}}), 4)
        True
    """
    n = num_of_nodes(graph)
    dist = [10 ** 19 for _ in range(n)]
    dist[start_node] = 0
    for _ in range(n):
        for u in graph:
            for x in graph[u]:
                distance = dist[u] + graph[u][x]
                if distance < dist[x]:
                    dist[x] = distance

    for u in graph:
        for x in graph[u]:
            if dist[u] + graph[u][x] < dist[x]:
                return True
    return False
