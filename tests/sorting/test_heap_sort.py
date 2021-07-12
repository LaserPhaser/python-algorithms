from algorithms.sorting.heap_sort import heap_sort


class TestHeapSort:
    def test_sort(self):
        array = [3, 17, 2, 21, 9]
        assert [2, 3, 9, 17, 21] == merge_sort(array)
        
