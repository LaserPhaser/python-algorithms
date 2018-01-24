"""
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph,
which may represent, for example, road networks.
It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later [Wikipedia]

Worst-case Performance: O(|E|+|V| log |V|)
"""
import queue


def dijkstra(graph, start, target):
    """
    Solves shortest path problem using Dijkstra algorithm
    Args:
        graph: graph representation
        start: start node
        target: target node

    Returns:
        int: distance between start and target nodes

    Examples:
        >>> graph = prepare_weighted_undirect_graph(
        [(1, 2, 7), (1, 3, 9), (1, 6, 14), (6, 3, 2), (6, 5, 9), (3, 2, 10), (3, 4, 11),
        (2, 4, 15), (6, 5, 9), (5, 4, 6)])

        >>> dijkstra(graph, 1, 6)
        11

    """
    dist = dict()
    dist[start] = 0
    q = queue.PriorityQueue()
    q.put(start)
    while not q.empty():
        node = q.get()
        for adjacent_node, edge_weigth in graph[node].items():
            length = dist[node] + edge_weigth
            if adjacent_node not in dist or length < dist[adjacent_node]:
                dist[adjacent_node] = length
                q.put(adjacent_node, dist[adjacent_node])
    if target not in dist:
        return -1
    return dist[target]
