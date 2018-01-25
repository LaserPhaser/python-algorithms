from algorithms.graphs import prepare_undirect_graph, prepare_direct_graph
from algorithms.graphs.dfs_cycle_detection import is_cyclic


class TestDFSCycleDetection:
    def test_direct_graph(self):
        edges = [(0, 1), (0, 2), (2, 3), (1, 3)]
        graph = prepare_direct_graph(edges)

        assert False is is_cyclic(graph), "Graph has no cycles"

    def test_undirect_graph(self):
        edges = [(0, 1), (0, 2), (2, 3), (1, 3)]
        graph = prepare_undirect_graph(edges)

        assert True is is_cyclic(graph), "Graph has  cycles"
