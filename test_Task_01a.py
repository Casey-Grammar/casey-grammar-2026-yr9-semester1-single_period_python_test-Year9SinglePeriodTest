import unittest
from Task_01a import calculate_total


class TestTask01a(unittest.TestCase):
    def test_whole_numbers(self):
        self.assertEqual(calculate_total(5, 2), 10)

    def test_decimal_price(self):
        self.assertEqual(calculate_total(4.5, 3), 13.5)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total(9.99, 0), 0)


if __name__ == "__main__":
    unittest.main()
