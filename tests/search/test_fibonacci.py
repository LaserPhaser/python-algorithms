from search.fibonacci import fibonacci as fibonacci_recursive
from search.fibonacci_modulo import fibonacci_modulo


class TestFibonacci:
    def test_recursive(self):
        assert fibonacci_recursive(20) == 6765, "Wrong answer for fibonacci of 20"

    def test_modulo(self):
        assert fibonacci_modulo(11527523930876953, 26673) == 10552, "Wrong answer for fibonacci modulo of 20"
