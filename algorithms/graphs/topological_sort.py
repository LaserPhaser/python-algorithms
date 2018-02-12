"""
In the field of computer science, a topological sort or topological ordering of a directed graph is a linear ordering
of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
[Wikipedia]
"""

from algorithms.graphs import prepare_direct_graph


class TopologicalSort:
    def __init__(self, edges):
        self._edges_num = len(edges)
        self._graph = prepare_direct_graph(edges)
        self._stack = set()
        self._ids = []
        self._visited = set()

    def _explore(self, vertex):
        """
        Function for exploring vertices neiborhoods and put them on stach
        Args:
            vertex: id of the vertex in the graph

        """
        if vertex in self._stack:
            return 1
        for adj_vertex in self._graph[vertex]:
            if adj_vertex not in self._visited:
                if self._explore(adj_vertex) == 1:
                    return
        self._visited.add(vertex)
        self._ids.append(vertex)

    def _dfs(self, edge_num):
        """
        Classical DFS algorithm for exploring vertices

        Args:
            edge_num: number of edges in the graph
        """
        for edge in range(edge_num):
            if edge not in self._visited:
                self._explore(edge)

    def sort(self):
        """
        Function do a topological sorting
        Returns: topologically sorted list of vertices
        """

        order = []
        self._dfs(self._edges_num)
        for i in self._ids[::-1]:
            order.append(i)

        return [vertex for vertex in order]
