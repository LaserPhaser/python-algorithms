import pytest

from algorithms.graphs import prepare_weighted_undirect_graph
from algorithms.graphs.dijkstra import dijkstra


class TestDijkstra:
    @pytest.mark.parametrize("start_point, target, distance",
                             [(1, 2, 7), (1, 3, 9), (1, 4, 20), (1, 5, 20), (1, 6, 11)])
    def test_small(self, start_point, target, distance):
        graph = prepare_weighted_undirect_graph(
            [(1, 2, 7), (1, 3, 9), (1, 6, 14), (6, 3, 2), (6, 5, 9), (3, 2, 10), (3, 4, 11),
             (2, 4, 15), (6, 5, 9), (5, 4, 6)])
        assert distance == dijkstra(graph, start_point, target), "Path distance is not correct"

    def test_start_eq_target(self):
        graph = prepare_weighted_undirect_graph(
            [(1, 2, 7), (1, 3, 9), (1, 6, 14), (6, 3, 2), (6, 5, 9), (3, 2, 10), (3, 4, 11),
             (2, 4, 15), (6, 5, 9), (5, 4, 6)])
        assert 0 == dijkstra(graph, 3, 3), "Path distance is not correct"

    def test_disconnected(self):
        graph = prepare_weighted_undirect_graph(
            [(1, 2, 7), (3, 4, 9)])
        assert -1 == dijkstra(graph, 1, 3), "Path distance is not correct"
