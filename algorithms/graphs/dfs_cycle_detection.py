"""
Detecting cycles in graph using DFS approach

https://en.wikipedia.org/wiki/Depth-first_search

"""


def _dfs_visit(graph, node, visited, stack):
    """
    Visit nodes in dfs order

    Args:
        graph: graph
        node: node to check
        visited: set of visited nodes
        stack: set of nodes on stack

    Returns:
        bool: True if cycles not found
              False if found

    """
    visited.add(node)
    stack.add(node)
    for neigborhood in graph[node]:
        if neigborhood not in visited:
            if _dfs_visit(graph, neigborhood, visited, stack):
                return True
        elif neigborhood in stack:
            return True
    stack.remove(node)
    return False


def is_cyclic(graph):
    """
    Detecting cycles in graph

    Args:
        graph: graph

    Returns:
        bool: True if cycles detected, False otherwise

    Examples:


    """
    visited = set()
    stack = set()
    for node in list(graph):
        if node not in visited:
            if _dfs_visit(graph, node, visited, stack):
                return True
    return False
