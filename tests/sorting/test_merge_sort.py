from algorithms.sorting.merge_sort import merge_sort


class TestMergeSort:
    def test_sort(self):
        array = [-1, 10, 3, -5.5, 11, 11.3]
        assert [-5.5, -1, 3, 10, 11, 11.3] == merge_sort(array)
