import unittest
from Task_02a import count_vowels


class TestTask02a(unittest.TestCase):
    def test_word(self):
        self.assertEqual(count_vowels("Education"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("sky"), 0)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("ApPlE"), 2)

    def test_empty(self):
        self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
