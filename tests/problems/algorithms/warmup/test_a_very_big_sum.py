import unittest
from src.problems.algorithms.warmup.a_very_big_sum.main import BigSum 

class TestBigSum(unittest.TestCase):
    def test_calculate_sum_with_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        big_sum = BigSum(numbers)
        result = big_sum.calculate_sum()
        self.assertEqual(result, 15)

    def test_calculate_sum_with_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        big_sum = BigSum(numbers)
        result = big_sum.calculate_sum()
        self.assertEqual(result, -15)

    def test_calculate_sum_with_mixed_numbers(self):
        numbers = [-1, 2, -3, 4, -5]
        big_sum = BigSum(numbers)
        result = big_sum.calculate_sum()
        self.assertEqual(result, -3)

    def test_calculate_sum_with_empty_list(self):
        numbers = []
        big_sum = BigSum(numbers)
        result = big_sum.calculate_sum()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
