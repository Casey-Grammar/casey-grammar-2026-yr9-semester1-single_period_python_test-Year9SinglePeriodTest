import unittest
from Task_02b import extract_even_numbers


class TestTask02b(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(extract_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_all_even(self):
        self.assertEqual(extract_even_numbers([2, 4, 8]), [2, 4, 8])

    def test_no_even(self):
        self.assertEqual(extract_even_numbers([1, 3, 5]), [])

    def test_empty_list(self):
        self.assertEqual(extract_even_numbers([]), [])


if __name__ == "__main__":
    unittest.main()
