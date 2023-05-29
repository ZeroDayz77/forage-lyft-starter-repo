import unittest

from tyre.carrigan_tyre import CarriganTyre


class TestCarriganTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tyre_wear = [0.5,0.7,1,0]
        tyre = CarriganTyre(tyre_wear)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyre_wear = [0.5,0.7,0.5,0.7]
        tyre = CarriganTyre(tyre_wear)
        self.assertFalse(tyre.needs_service())