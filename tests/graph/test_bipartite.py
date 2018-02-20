from algorithms.graphs import prepare_undirect_graph
from algorithms.graphs.bipartite import bipartite


class TestBipartite:
    def test_false(self):
        graph = prepare_undirect_graph([(1, 2), (3, 1), (2, 3), (4, 1)])
        assert False is bipartite(graph), 'Wrong bipartite detection'

    def test_true(self):
        graph = prepare_undirect_graph([(1, 4), (3, 4), (2, 4), (2, 5)])
        assert True is bipartite(graph), 'Wrong bipartite detection'
