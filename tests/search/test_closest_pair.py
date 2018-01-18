import random

from algorithms.search.closest_pair import brute_force_distance, n_log_n_squared_distance


class TestClosestPair:
    def test_n_log_n_squared_distance(self):
        points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        assert 1.414214 == round(n_log_n_squared_distance(points), 6), 'N (log N) ^2 solution is not wirking '

    def test_brute_force_distance(self):
        points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        assert 1.414214 == round(brute_force_distance(points), 6), 'Brute force solution is not working'

    def test_random_10000_pairs(self):
        points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(100)]
        assert brute_force_distance(points) == n_log_n_squared_distance(points), 'Brute force solution is not equal' \
                                                                                 ' to N (log N) ^2 solution'
