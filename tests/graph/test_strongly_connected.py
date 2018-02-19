from algorithms.graphs import prepare_direct_graph
from algorithms.graphs.strongly_connected import StronglyConnected


class TestSCC:
    def test_graph(self):
        graph = prepare_direct_graph([(0, 2), (2, 1), (1, 0), (0, 3), (3, 4)])
        assert [[0, 1, 2], [3], [4]] == StronglyConnected(
            graph).strongly_connected_components(), 'Error in detecting SCC'
