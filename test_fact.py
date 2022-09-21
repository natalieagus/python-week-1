import unittest
from Q1_fact import factorial_iteration


class LargestRangeTest(unittest.TestCase):
    def test_fact_default(
        self,
    ):
        data = 10
        result = factorial_iteration(data)
        self.assertEqual(result, 3628800)

    def test_fact_zero(
        self,
    ):
        data = 0
        result = factorial_iteration(data)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
