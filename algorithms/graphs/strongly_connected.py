"""
In the mathematical theory of directed graphs, a graph is said to be strongly connected or diconnected if every
vertex is reachable from every other vertex.
"""
import sys

from algorithms.graphs import reverse_graph, get_nodes

sys.setrecursionlimit(200000)


class StronglyConnected:

    def __init__(self, graph):
        self._reached = set()
        self._visited = set()
        self._stack = []
        self.graph = graph
        self._components = []

    def _explore(self, node):
        """
        Heler function - marks explored adjacent nodes in graph as reached and adds them on stack

        Args:
            node: node to check neighbourhoods

        """
        self._components.append(node)
        self._visited.add(node)
        for adj in self.graph[node]:
            if adj not in self._reached and adj not in self._visited:
                self._explore(adj)
        self._reached.add(node)
        self._visited.remove(node)
        self._stack.append(node)

    def _dfs(self, graph):
        """
        Helper function - classical DFS algorithm fro graph traversal

        Args:
            graph:  graph representation
        """
        nodes = get_nodes(graph)
        for node in nodes:
            if node not in self._reached:
                self._explore(node)

    def strongly_connected_components(self):
        """
        Function finds, and return list of SCC in the graph

        Returns:
            list: SCC

        Examples:
            >>> graph = prepare_direct_graph([(0, 2), (2, 1), (1, 0), (0, 3), (3, 4)])
            >>> StronglyConnected(graph).strongly_connected_components()
            [[0, 1, 2], [3], [4]]

        """
        scc = []
        rev_graph = reverse_graph(self.graph)
        self._dfs(rev_graph)
        self._reached = set()
        self.graph = rev_graph
        while self._stack:
            node = self._stack.pop()
            if node not in self._reached:
                self._components = []
                self._explore(node)
                scc.append(self._components)

        return scc
