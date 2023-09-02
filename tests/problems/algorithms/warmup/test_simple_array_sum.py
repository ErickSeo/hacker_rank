import unittest
from src.problems.algorithms.warmup.simple_array_sum.main import SimpleArraySum

class TestSimpleArraySum(unittest.TestCase):
    def setUp(self):
        self.simple_array = SimpleArraySum()

    def test_total_with_empty_list(self):
        self.assertEqual(self.simple_array.total(), 0)

    def test_total_with_single_number(self):
        self.simple_array.numbers = 5
        self.assertEqual(self.simple_array.total(), 5)

    def test_total_with_multiple_numbers(self):
        self.simple_array.numbers = 2
        self.simple_array.numbers = 3
        self.simple_array.numbers = 4
        self.assertEqual(self.simple_array.total(), 9)

if __name__ == '__main__':
    unittest.main()
