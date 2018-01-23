from algorithms.graphs import prepare_undirect_graph, prepare_direct_graph
from algorithms.graphs.bfs import bfs_iterative


class TestBFSIterative:
    def test_direct_graph(self):
        edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
        graph = prepare_direct_graph(edges)
        assert [2, 0, 3, 1] == bfs_iterative(graph, 2), "Order of vertex visiting is wrong"

    def test_undirect_graph(self):
        edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
        graph = prepare_undirect_graph(edges)
        assert [2, 0, 1, 3] == bfs_iterative(graph, 2), "Order of vertex visiting is wrong"

    def test_direct_graph_2(self):
        edges = [(1, 2), (2, 5), (2, 4), (4, 6), (4, 5), (5, 3), (3, 1)]
        graph = prepare_direct_graph(edges)
        assert [1, 2, 4, 5, 6, 3] == bfs_iterative(graph, 1), "Order of vertex visiting is wrong"

    def test_undirect_graph_2(self):
        edges = [(1, 2), (2, 5), (2, 4), (4, 6), (4, 5), (5, 3), (3, 1)]
        graph = prepare_undirect_graph(edges)
        assert [1, 2, 3, 4, 5, 6] == bfs_iterative(graph, 1), "Order of vertex visiting is wrong"
