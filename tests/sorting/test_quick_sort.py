from algorithms.sorting.quick_sort import quick_sort


class TestQuckSort:
    def test_sort(self):
        array = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
        low = 0
        high = len(array) - 1

        assert [1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 9, 9, 9] == quick_sort(array, low, high)

    def test_sort_float(self):
        array = [1, 10, 32, 4.]
        low = 0
        high = len(array) - 1
        assert [1, 4.0, 10, 32] == quick_sort(array, low, high)
