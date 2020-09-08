from unittest import TestCase
from numpy import array, ndarray
from numpy.testing import assert_array_equal
from trigger import trigger_time


class TriggerTimeTest(TestCase):
    def test_estimates_when_function_exceeds(self):
        function = 10
        t = array([1599574034])
        trig_level = 100
        expected = ndarray([])
        actual = trigger_time(function, t, trig_level)
        assert_array_equal(expected, actual)
