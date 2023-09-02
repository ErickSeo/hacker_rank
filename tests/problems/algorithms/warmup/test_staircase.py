import unittest
from io import StringIO
import sys
from src.problems.algorithms.warmup.staircase.main import Staircase

class TestStaircase(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.held_output.close()

    def test_build_staircase(self):
        staircase = Staircase(size=5)
        expected_output = "    #\n   ##\n  ###\n ####\n#####\n"
        staircase.build()
        self.assertEqual(self.held_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
