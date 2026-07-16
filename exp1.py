class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed books

    def __str__(self):
        return f"Patron: {self.name}"

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Registered: {patron}")

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f"{patron.name} returned {book.title}.")
        else:
            print(f"{patron.name} does not have {book.title}.")


            # --- Demonstration of the System ---
if __name__ == "__main__":
    # Initialize Library
    my_library = Library()

    # Create Books and Patrons
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    patron1 = Patron("Alice")

    # Perform Operations
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.register_patron(patron1)

    print("\n--- Borrowing Process ---")
    my_library.borrow_book(patron1, book1)

    print("\n--- Returning Process ---")
    my_library.return_book(patron1, book1)

