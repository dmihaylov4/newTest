import unittest

from nums import closest_to_zero

class TestClosestToZero(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(closest_to_zero([3, 2, -2, -3, 1]), 1)
        self.assertEqual(closest_to_zero([-3, -2, -1]), -1)
        self.assertEqual(closest_to_zero([0]), 0)

    def test_empty(self):
        self.assertIsNone(closest_to_zero([]))

    def test_large_values(self):
        self.assertEqual(closest_to_zero([1000000, -1000001]), 1000000)

if __name__ == "__main__":
    unittest.main()