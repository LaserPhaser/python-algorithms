from algorithms.greedy.covering_segments import covering_segments


class TestCoveringSegments:
    def test_simple(self):
        assert covering_segments([(1, 3), (2, 5), (3, 6)]) == [3], "Coordinate of found point is not equal to 3"

    def test_disjoint(self):
        assert covering_segments([(4, 7), (1, 3), (2, 5), (5, 6)]) == [3, 6], "Coordinate of found points are not " \
                                                                              "equal to 3, 6"

    def test_minimal(self):
        assert covering_segments([(0, 0)]) == [0], "Coordinate of found point is not equal to 0"

    def test_negative(self):
        assert covering_segments(
            [(0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (-1, 2)]) == [2], "Coordinate of found point is not equal to 2"
