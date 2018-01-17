from algorithms.greedy.fractional_knapsack import fractional_knapsack


class TestFractionalKnapsack:
    def test_simple(self):
        assert fractional_knapsack(50, [(60, 10), (100, 20), (120, 30)]) == 240.
