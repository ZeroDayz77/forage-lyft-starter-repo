import unittest

from tyre.octoprime_tyre import OctoprimeTyre

class TestOctoprimeTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tyre_wear = [1,1,1,0]
        tyre = OctoprimeTyre(tyre_wear)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyre_wear = [1,1,0,0]
        tyre = OctoprimeTyre(tyre_wear)
        self.assertFalse(tyre.needs_service())