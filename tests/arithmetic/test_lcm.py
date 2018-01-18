import pytest

from algorithms.arithmetic.lcm import lcm


class TestLCM:
    def test_simple(self):
        assert lcm(16, 20) == 80, "LCM of 16, 20 is not 80"

    def test_simple_reverse(self):
        assert lcm(20, 16) == 80, "LCM of 20, 16 is not 80"

    def test_multi_digits(self):
        assert lcm(8, 9, 21) == 504, "LCM of 8, 9, 21 is not 504"

    @pytest.mark.parametrize("x1, x2", [(0, 1), (1, 0), (0, 0), (-1, - 1)])
    def test_value_error(self, x1, x2):
        with pytest.raises(ValueError):
            lcm(x1, x2)

    @pytest.mark.parametrize("x1, x2", [(1.0, 1), (1, 1.0), ('string', 0), ([1, 2], 2)])
    def test_type_error(self, x1, x2):
        with pytest.raises(TypeError):
            lcm(x1, x2)
