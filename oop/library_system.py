# library_system.py

class Book:
    """A base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class representing an eBook, inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class representing a printed book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class representing a library that manages a collection of books."""
    def __init__(self):
        self.books = []  # List to store books (Book, EBook, and PrintBook)

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
