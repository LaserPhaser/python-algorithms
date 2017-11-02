import pytest

from arithmetic.gcd import gcd


class TestGCD:
    def test_simple_gcd(self):
        assert gcd(54, 24) == 6, "GCD of 54 x 23 is not 6"

    @pytest.mark.parametrize("x1, x2", [(0, 1), (1, 0), (0, 0), (-1, - 1)])
    def test_value_error_gcd(self, x1, x2):
        try:
            gcd(x1, x2)
        except ValueError as error:
            assert str(error) == 'GCD is not support negative numbers and zeros'
        else:
            raise AssertionError('ValueError was not raised')

    @pytest.mark.parametrize("x1, x2", [(1.0, 1), (1, 1.0), ('string', 0), ([1, 2], 2)])
    def test_type_error_gcd(self, x1, x2):
        try:
            gcd(x1, x2)
        except TypeError as error:
            assert str(error) == 'GCD function support only integer types'
        else:
            raise AssertionError('TypeError was not raised')

    def test_minimum_gcd(self):
        assert gcd(7, 3) == 1, "GCD of 7 x 3 is not 1"

    def test_large_gcd(self):
        assert gcd(978, 89798763754892653453379597352537489494736) == 6, \
            "GCD of 978 x 89798763754892653453379597352537489494736 is not 6"
