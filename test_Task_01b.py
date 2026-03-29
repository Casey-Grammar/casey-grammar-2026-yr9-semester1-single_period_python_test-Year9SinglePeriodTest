import unittest
from Task_01b import classify_temperature


class TestTask01b(unittest.TestCase):
    def test_cold(self):
        self.assertEqual(classify_temperature(10), "Cold")

    def test_mild(self):
        self.assertEqual(classify_temperature(20), "Mild")

    def test_hot(self):
        self.assertEqual(classify_temperature(30), "Hot")


if __name__ == "__main__":
    unittest.main()
