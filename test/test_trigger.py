from unittest import TestCase
from numpy import array
from numpy.testing import assert_array_equal
from trigger import sta_lta

class TestStaLta(TestCase):
    def test_it_provides_the_right_value(self):
        x = array([1, 2, 3])
        nsta = 1
        nlta = 1
        expected = [1, 1, 1]
        actual = sta_lta(x, nsta, nlta)
        assert_array_equal(expected, actual)
