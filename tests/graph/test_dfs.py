from algorithms.graphs import prepare_undirect_graph, prepare_direct_graph
from algorithms.graphs.dfs import dfs_iterative


class TestDFSIterative:
    def test_direct_graph(self):
        edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
        graph = prepare_direct_graph(edges)
        assert [2, 3, 0, 1] == dfs_iterative(graph, 2), "Order of vertex visiting is wrong"

    def test_direct_graph_3(self):
        edges = [(1, 0), (0, 2), (2, 1), (0, 3), (1, 4)]
        graph = prepare_direct_graph(edges)
        assert [0, 3, 2, 1, 4] == dfs_iterative(graph, 0), "Order of vertex visiting is wrong"

    def test_undirect_graph(self):
        edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
        graph = prepare_undirect_graph(edges)
        print(graph)
        assert [2, 3, 1, 0] == dfs_iterative(graph, 2), "Order of vertex visiting is wrong"

    def test_direct_graph_2(self):
        edges = [(1, 2), (2, 5), (2, 4), (4, 6), (4, 5), (5, 3), (3, 1)]
        graph = prepare_direct_graph(edges)
        assert [1, 2, 5, 3, 4, 6] == dfs_iterative(graph, 1), "Order of vertex visiting is wrong"

    def test_undirect_graph_2(self):
        edges = [(1, 2), (2, 5), (2, 4), (4, 6), (4, 5), (5, 3), (3, 1)]
        graph = prepare_undirect_graph(edges)
        assert [1, 3, 5, 4, 6, 2] == dfs_iterative(graph, 1), "Order of vertex visiting is wrong"

    def test_direct_graph_3(self):
        edges = [(1, 2), (2, 3), (1, 4), (4, 5), (1, 6), (6, 7), (1, 8), (7, 9)]
        graph = prepare_undirect_graph(edges)
        assert [1, 8, 6, 7, 9, 4, 5, 2, 3] == dfs_iterative(graph, 1), "Order of vertex visiting is wrong"
