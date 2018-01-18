from algorithms.greedy.fractional_knapsack import fractional_knapsack


class TestFractionalKnapsack:
    def test_simple(self):
        assert fractional_knapsack(50, [(60, 10), (100, 20), (120, 30)]) == 240., "Returned value is not correct"

    def test_0_capacity(self):
        assert fractional_knapsack(0, [(1, 1)]) == 0.0, "Returned value is not correct"
