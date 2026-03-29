import unittest
from Task_05a import find_largest


class TestTask05a(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(find_largest([4, 9, 2, 7]), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_largest([-5, -1, -9]), -1)

    def test_single_number(self):
        self.assertEqual(find_largest([12]), 12)


if __name__ == "__main__":
    unittest.main()
