import unittest
from largest_range import find_largest_range


class LargestRangeTest(unittest.TestCase):
    def test_find_largest_range_default(
        self,
    ):  # function name begins with test
        """
        Test that it can find the largest range in the list
        """
        data = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
        result = find_largest_range(data)
        self.assertEqual(result, [0, 7])

    def test_find_largest_range_negative(
        self,
    ):  
        data = [8, -4, 200, 10, 3, 6, 7, 9, 1, 0, -55]
        result = find_largest_range(data)
        self.assertEqual(result, [6, 10])

    def test_find_largest_range_empty(self):
        data = []
        result = find_largest_range(data)
        self.assertEqual(result, [])

    def test_find_largest_range_single_element(self):
        data = [5]
        result = find_largest_range(data)
        self.assertEqual(result, [5, 5])


if __name__ == "__main__":
    unittest.main()
