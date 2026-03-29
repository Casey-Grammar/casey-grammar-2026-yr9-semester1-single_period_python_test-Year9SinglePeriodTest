import unittest
from Task_04 import expand_subject_codes


class TestTask04(unittest.TestCase):
    def test_valid_codes(self):
        self.assertEqual(
            expand_subject_codes(["MAT", "SCI", "ENG"]),
            ["Mathematics", "Science", "English"]
        )

    def test_invalid_codes_ignored(self):
        self.assertEqual(
            expand_subject_codes(["MAT", "XYZ", "ART"]),
            ["Mathematics", "Art"]
        )

    def test_lowercase_input(self):
        self.assertEqual(
            expand_subject_codes(["eng", "his"]),
            ["English", "History"]
        )

    def test_empty_list(self):
        self.assertEqual(expand_subject_codes([]), [])


if __name__ == "__main__":
    unittest.main()
