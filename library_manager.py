# library_manager.py

class Book:
    def __init__(self, title: str, author: str, year: int, copies: int = 1):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.copies} copies available"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, year: int, copies: int = 1):
        # Check if book already exists
        for book in self.books:
            if book.title == title and book.author == author:
                book.copies += copies
                return f"Added {copies} more copies of '{title}'."
        # If not, add a new book
        new_book = Book(title, author, year, copies)
        self.books.append(new_book)
        return f"Added '{title}' by {author}."

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"'{title}' removed from the library."
        return f"Book '{title}' not found in the library."

    def search_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return f"Book '{title}' not found."

    def list_books(self):
        if not self.books:
            return "The library has no books."
        return "\n".join(str(book) for book in self.books)


#Testando o GitActions