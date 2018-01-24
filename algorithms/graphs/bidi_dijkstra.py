"""
Bidirectional search is a graph search algorithm that finds a shortest path from an initial vertex to a goal
vertex in a directed graph. It runs two simultaneous searches: one forward from the initial state
, and one backward from the goal, stopping when the two meet in the middle. [Wikipedia]

"""
import queue


def _visit(direction_queues, side, node, dist, length):
    """
    Function for adding length of the path to the queueues

    Args:
        direction_queues: queues
        side: which side needs to be processed (from tartget or from source)
        node: node itself
        dist: distances array
        length: lenght of the path


    """
    if node not in dist[side] or dist[side][node] > length:
        dist[side][node] = length
        direction_queues[side].put((length, node))


def bidi_dijkstra(graph, start, target):
    """
    Calculate shortest path via Dijkstra algorithm, with bidirectional optimization
    which means that we start from target and start points and swith between them each step

    Args:
        graph: graph representation
        start: start node
        target: target node

    Returns:
        int: lengths of the shortest path between start and target nodes


    Examples:
    >>> graph = prepare_weighted_undirect_graph(
    [(1, 2, 7), (1, 3, 9), (1, 6, 14), (6, 3, 2), (6, 5, 9), (3, 2, 10), (3, 4, 11),
    (2, 4, 15), (6, 5, 9), (5, 4, 6)])

    >>> dijkstra(graph, 1, 6)
    11
    """
    dist = [dict(), dict()]
    visits = [set(), set()]
    direction_queues = [queue.PriorityQueue(), queue.PriorityQueue()]
    _visit(direction_queues, 0, start, dist, 0)
    _visit(direction_queues, 1, target, dist, 0)
    nodes_process = [[], []]
    flip_side = 0
    while not direction_queues[0].empty() or not direction_queues[1].empty():
        node = direction_queues[flip_side].get()[1]
        for adjacent_node, edge_weigth in graph[node].items():
            length = dist[flip_side][node] + edge_weigth
            _visit(direction_queues, flip_side, adjacent_node, dist, length)
        nodes_process[flip_side].append(node)
        visits[flip_side].add(node)
        if node in visits[flip_side ^ 1]:
            return _calc_shortest_path(nodes_process, dist)
        if not direction_queues[flip_side ^ 1].empty():
            flip_side ^= 1

    return -1


def _calc_shortest_path(nodes_process, dist):
    """
    Calculate shortest path

    Args:
        nodes_process: nodes that we met on path
        dist: distances

    Returns:
        int: length shortest path

    """
    shortest_path = 10 ** 16
    for node in nodes_process[1] + nodes_process[0]:

        if node in dist[0] and node in dist[1] and dist[0][node] + dist[1][node] < shortest_path:
            shortest_path = dist[0][node] + dist[1][node]
    return shortest_path
