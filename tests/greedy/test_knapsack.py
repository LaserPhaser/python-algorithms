from dynamic_programming import knapsack


class TestKnapsack:
    def test_simple(self):
        capacity = 165
        weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
        assert knapsack.optimal_weight(capacity, weights) == 165, "Weight is not equal to capacity, for current test"
