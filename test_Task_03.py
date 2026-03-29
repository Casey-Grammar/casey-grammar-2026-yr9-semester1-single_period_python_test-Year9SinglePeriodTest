import unittest
from Task_03 import replace_book


class TestTask03(unittest.TestCase):
    def test_replace_existing(self):
        books = ["Wonder", "Holes", "Matilda"]
        self.assertEqual(
            replace_book(books, "Holes", "Hatchet"),
            ["Wonder", "Hatchet", "Matilda"]
        )

    def test_not_found(self):
        books = ["Wonder", "Holes", "Matilda"]
        self.assertEqual(
            replace_book(books, "Diary of a Wimpy Kid", "Hatchet"),
            ["Wonder", "Holes", "Matilda"]
        )

    def test_first_occurrence_only(self):
        books = ["Holes", "Wonder", "Holes"]
        self.assertEqual(
            replace_book(books, "Holes", "Hatchet"),
            ["Hatchet", "Wonder", "Holes"]
        )

    def test_empty_list(self):
        self.assertEqual(replace_book([], "Holes", "Hatchet"), [])


if __name__ == "__main__":
    unittest.main()
