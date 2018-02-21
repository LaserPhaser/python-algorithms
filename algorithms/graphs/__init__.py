from collections import defaultdict, namedtuple


def prepare_undirect_graph(edges):
    """
    Function for converting list of edges to dict graph representation

    Args:
        edges: list of tuples, example: [(1,2), (2,3)]

    Returns:
        Defaultdict(list): that represent graph

    Examples:
        >>> prepare_undirect_graph([(1, 2), (3, 4), (2, 4), (2, 3)])
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
        >>> prepare_direct_graph([(1, 2), (3, 4), (2, 4), (2, 3)])
        defaultdict(list, {1: [2], 2: [1, 3, 4], 3: [2, 4], 4: [2, 3]})

    """

    graph = defaultdict(list)

    for (vertex_a, vertex_b) in edges:
        graph[vertex_a].append(vertex_b)
    graph = __sort_default_dict(graph)
    return graph


def prepare_weighted_undirect_graph(edges):
    """
    Function for conveting list of edges with weights to dict graph representation
    Args:
        edges: list of tuples, example [(1, 2, 3), (3, 2, 1)]; [(node_a, node_b, weight)]

    Returns:
        >>> prepare_weighted_undirect_graph([(1, 2, 1), (4, 1, 2), (2, 3, 2), (1, 3, 5) ])
        defaultdict(<class 'dict'>, {1: {2: 1, 4: 2, 3: 5}, 2: {1: 1, 3: 2}, 4: {1: 2}, 3: {2: 2, 1: 5}})

    """

    graph = defaultdict(dict)

    for (vertex_a, vertex_b, weight) in edges:
        graph[vertex_a].update(({vertex_b: weight}))
        graph[vertex_b].update(({vertex_a: weight}))

    return graph


def prepare_weighted_direct_graph(edges):
    """
    Function for conveting list of edges with weights to dict graph representation
    Args:
        edges: list of tuples, example [(1, 2, 3), (3, 2, 1)]; [(node_a, node_b, weight)]

    Returns:
        >>> prepare_weighted_direct_graph([(1, 2, 1), (4, 1, 2), (2, 3, 2), (1, 3, 5)])
        defaultdict(dict, {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}})

    """

    graph = defaultdict(dict)

    for (vertex_a, vertex_b, weight) in edges:
        graph[vertex_a].update(({vertex_b: weight}))

    return graph


def reverse_weighted_graph(graph):
    """
    Function for reverting direction of the graph (weights still the same)

    Args:
        graph: graph representation as Example: {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}}

    Returns:
        reversed graph

    Examples:
        >>> reverse_weighted_graph({1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}})
        defaultdict(<class 'dict'>, {2: {1: 1}, 3: {1: 5, 2: 2}, 1: {4: 2}})

    """
    rev_graph = defaultdict(dict)
    for node, neighborhood in graph.items():
        for adj, weight in neighborhood.items():
            rev_graph[adj].update(({node: weight}))
    return rev_graph


def reverse_graph(graph):
    """
    Function for reverting direction of the graph

    Args:
        graph: graph representation as Example: [(1, 2), (3, 4), (2, 4), (2, 3)]

    Returns:
        reversed graph

    Examples:
        >>> reverse_graph({1: [2], 2: [1, 3, 4], 3: [2, 4], 4: [2, 3]})
        defaultdict(<class 'list'>, {2: [1, 3, 4], 1: [2], 3: [2, 4], 4: [2, 3]})

    """
    rev_graph = defaultdict(list)
    for node, neighborhood in graph.items():
        for adj in neighborhood:
            rev_graph[adj].append(node)
    return rev_graph


def get_nodes(graph):
    """
    Function for calculating number of nodes in the graph

    Args:
        graph: graph representation as Example: {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}}

    Returns:
        nodes of the graph


    """
    return __nodes_and_edges(graph).nodes


def num_of_nodes(graph):
    """
    Function for calculating number of nodes in the graph

    Args:
        graph: graph representation as Example: {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}}

    Returns:
        number of nodes in the graph


    """
    return len(get_nodes(graph))


def get_edges(graph):
    """
    Function for calculating number of edges

    Args:
        graph: graph representation as Example: {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}}

    Returns:
        edges of the graph

    """
    return __nodes_and_edges(graph).edges


def num_of_edges(graph):
    """
    Function for calculating number of edges

    Args:
        graph: graph representation as Example: {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}}

    Returns:
        number of the edges in the graph

    """
    return len(get_edges(graph))


def __nodes_and_edges(graph):
    """
    Function for calculating number of nodes and edges in the graph

    Args:
        graph: graph representation as Example: {1: {2: 1, 3: 5}, 2: {3: 2}, 4: {1: 2}}

    Returns:
        namedtuple[nodes, edges]: nodes and the edges in the graph


    """
    GraphData = namedtuple('GData', ['nodes', 'edges'])
    nodes = set()
    edges = set()
    for node, neighborhood in graph.items():
        nodes.add(node)
        if isinstance(neighborhood, dict):
            for adj, weight in neighborhood.items():
                nodes.add(adj)
                edges.add((node, adj))
        elif isinstance(neighborhood, list):
            for adj in neighborhood:
                nodes.add(adj)
                edges.add((node, adj))
    graph_data = GraphData(nodes, edges)
    return graph_data


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
