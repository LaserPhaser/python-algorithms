import pytest

from algorithms.graphs.topological_sort import TopologicalSort


class TestDFSIterative:
    @pytest.mark.parametrize('edges, sorted', [([(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)], [5, 4, 2, 3, 1, 0]),

                                               ([(2, 1), (4, 3), (4, 1), (5, 2), (5, 3)],
                                                [4, 3, 2, 1, 0])])
    def test_graph(self, edges, sorted):
        assert sorted == TopologicalSort(edges).sort(), 'Error in topological sorting please check the algorithm'
