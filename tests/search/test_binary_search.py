from algorithms.search.binary_search import binary_search


class TestBinarySearch:
    def test_not_found(self):
        assert binary_search([1, 2, 3, 4], 5) == -1, "Expected value (-1) was not returned"

    def test_simple(self):
        assert binary_search([x for x in range(10000)], 26) == 26, "Expected value (26) was not returned"
