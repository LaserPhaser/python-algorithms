"""
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key')
and explores the neighbor nodes first, before moving to the next level neighbours. [Wikipedia]

Worst-case performance:	O(V + E) = O(b^d)

Worst-case space complexity O(V) = O(b^d)

https://wikipedia.org/wiki/Breadth-first_search
"""


def bfs_iterative(graph, root):
    """
    Iterative version of the BFS algorithm

    Args:
        graph: dict representation of the graph
        root: start point


    Returns:
        list: in order of visiting vertices

    Examples:


    """
    node_queue = []
    visited = set()
    visiting_sequence = []
    node_queue.append(root)
    visited.add(root)
    while node_queue:
        v = node_queue.pop(0)
        visiting_sequence.append(v)
        for x in graph[v]:
            if x not in visited:
                visited.add(x)
                node_queue.append(x)

    return visiting_sequence
