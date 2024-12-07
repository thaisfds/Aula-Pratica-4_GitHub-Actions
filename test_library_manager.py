# test_library_manager.py

import unittest
from library_manager import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        result = self.library.add_book("Python Programming", "John Doe", 2020, 3)
        self.assertEqual(result, "Added 'Python Programming' by John Doe.")
        self.assertEqual(len(self.library.books), 1)

    def test_add_duplicate_book(self):
        self.library.add_book("Python Programming", "John Doe", 2020, 3)
        result = self.library.add_book("Python Programming", "John Doe", 2020, 2)
        self.assertEqual(result, "Added 2 more copies of 'Python Programming'.")
        self.assertEqual(self.library.books[0].copies, 5)

    def test_remove_book(self):
        self.library.add_book("Python Programming", "John Doe", 2020)
        result = self.library.remove_book("Python Programming")
        self.assertEqual(result, "'Python Programming' removed from the library.")
        self.assertEqual(len(self.library.books), 0)

    def test_remove_nonexistent_book(self):
        result = self.library.remove_book("Nonexistent Book")
        self.assertEqual(result, "Book 'Nonexistent Book' not found in the library.")

    def test_search_book(self):
        self.library.add_book("Python Programming", "John Doe", 2020)
        book = self.library.search_book("Python Programming")
        self.assertEqual(book.title, "Python Programming")

    def test_search_nonexistent_book(self):
        result = self.library.search_book("Nonexistent Book")
        self.assertEqual(result, "Book 'Nonexistent Book' not found.")

    def test_list_books(self):
        self.library.add_book("Python Programming", "John Doe", 2020)
        self.library.add_book("Data Science", "Jane Smith", 2019)
        result = self.library.list_books()
        self.assertIn("Python Programming", result)
        self.assertIn("Data Science", result)

    def test_list_no_books(self):
        result = self.library.list_books()
        self.assertEqual(result, "The library has no books.")

if __name__ == "__main__":
    unittest.main()
