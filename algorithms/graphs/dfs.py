"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores
 as far as possible along each branch before backtracking. [Wikipedia]

Worst-case performance:	O(V + E) = O(b^d)

Worst-case space complexity O(V) = O(b^d)

https://en.wikipedia.org/wiki/Depth-first_search
"""


def dfs_iterative(graph, root):
    """
    Iterative version of the DFS algorithm

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
    visiting_sequence.append(root)
    while node_queue:
        v = node_queue.pop()
        if v not in visited:
            visited.add(v)
            visiting_sequence.append(v)
        for x in graph[v]:
            if x not in visited:
                node_queue.append(x)

    return visiting_sequence
