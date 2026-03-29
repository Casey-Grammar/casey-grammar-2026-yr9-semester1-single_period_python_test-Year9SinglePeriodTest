import unittest
from Task_05b import unique_items


class TestTask05b(unittest.TestCase):
    def test_duplicates_removed(self):
        self.assertEqual(
            unique_items(["pen", "book", "pen", "ruler", "book"]),
            ["pen", "book", "ruler"]
        )

    def test_no_duplicates(self):
        self.assertEqual(
            unique_items(["apple", "banana", "orange"]),
            ["apple", "banana", "orange"]
        )

    def test_all_same(self):
        self.assertEqual(
            unique_items(["chair", "chair", "chair"]),
            ["chair"]
        )

    def test_empty_list(self):
        self.assertEqual(unique_items([]), [])


if __name__ == "__main__":
    unittest.main()
