"""
In the mathematical field of graph theory, a bipartite graph (or bigraph) is a graph whose vertices can be divided
into two disjoint and independent sets  U and  V such that every edge
connects a vertex in U to one in {\displaystyle V} V. Vertex sets U and  V are usually called the parts of the graph.
Equivalently, a bipartite graph is a graph that does not contain any odd-length cycles. [Wikipedia]
"""
import queue
from collections import defaultdict


def bipartite(graph):
    """
    Function checks if graph is bipartite

    Args:
        graph: graph representation

    Returns:
        bool: True if bipartite , False otherwise
    """
    color = defaultdict(int)
    visited = set()
    node_queue = queue.Queue()
    start_node = list(graph.keys())[0]
    color[start_node] = 1
    visited.add(start_node)
    node_queue.put(start_node)
    while not node_queue.empty():
        vertex_from_queue = node_queue.get()
        for adjacent_node in graph[vertex_from_queue]:
            if adjacent_node in visited and color[adjacent_node] == color[vertex_from_queue]:
                return False
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                color[adjacent_node] = color[vertex_from_queue] * -1
                node_queue.put(adjacent_node)
    return True
