from algorithms.graphs import prepare_weighted_direct_graph
from algorithms.graphs.bellman_ford_negative_cycle import negative_cycle


class TestBellmanFordNegativeCycleDetection:
    def test_negative_cycle_graph(self):
        edges = [(0, 1, 1),
                 (1, 2, -1),
                 (2, 3, -1),
                 (3, 0, -1)]
        graph = prepare_weighted_direct_graph(edges)
        print(graph)
        assert True is negative_cycle(graph, 4), "Graph has no cycles"

    def test_no_negative_cycle_graph(self):
        edges = [(0, 1, -1),
                 (0, 2, 4),
                 (1, 2, 3),
                 (1, 3, 2),
                 (1, 4, 2),
                 (3, 2, 5),
                 (3, 1, 1),
                 (4, 3, -3)]
        graph = prepare_weighted_direct_graph(edges)

        assert False is negative_cycle(graph, 5), "Graph has  cycles"
