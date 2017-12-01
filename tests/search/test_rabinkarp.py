from search.rabinkarp import rabin_karp


class TestRabinKarp:
    def test_simple(self):
        assert rabin_karp('aaaaa', 'aaa') == [0, 1, 2], "Did not find proper idx in string"

    def test_overlapping(self):
        assert rabin_karp('AABAACAADAABAABA', 'AABA') == [0, 9, 12], "Did not find proper idx in string"
