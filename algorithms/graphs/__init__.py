from collections import defaultdict


def prepare_undirect_graph(edges):
    """
    Function for converting list of edges to dict graph representation
    
    Args:
        edges: list of tuples, example: [(1,2), (2,3)] 

    Returns:
        Defaultdict(list): that represent graph

    Examples:
        >>> prepare_graph([(1, 2), (3, 4), (2, 4), (2, 3)])
        defaultdict(list, {1: [2], 2: [1, 3, 4], 3: [2, 4], 4: [2, 3]})

    """

    graph = defaultdict(list)

    for (vertex_a, vertex_b) in edges:
        graph[vertex_a].append(vertex_b)
        graph[vertex_b].append(vertex_a)
    graph = __sort_default_dict(graph)
    return graph


def prepare_direct_graph(edges):
    """
    Function for converting list of edges to dict graph representation

    Args:
        edges: list of tuples, example: [(1,2), (2,3)]

    Returns:
        Defaultdict(list): that represent graph

    Examples:
        >>> prepare_graph([(1, 2), (3, 4), (2, 4), (2, 3)])
        defaultdict(list, {1: [2], 2: [1, 3, 4], 3: [2, 4], 4: [2, 3]})

    """

    graph = defaultdict(list)

    for (vertex_a, vertex_b) in edges:
        graph[vertex_a].append(vertex_b)
    graph = __sort_default_dict(graph)
    return graph


def __sort_default_dict(graph):
    """
    Sorts lists elements of defaultdict(list)
    Args:
        graph: defaultdict(list)

    Returns:
        Sorted list elements of defaultdict(list)
    """
    for x in graph:
        graph[x] = sorted(graph[x])
    return graph
