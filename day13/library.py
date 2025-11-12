class Library:
    
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to the library!")

    def show_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available Books:", ", ".join(self.books))

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You borrowed '{book_name}'.")
        else:
            print("Book not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"You returned '{book_name}'.")


# --- Create and use Library object ---
my_library = Library()

my_library.add_book("Python Basics")
my_library.add_book("Data Structures")
my_library.show_books()

my_library.borrow_book("Python Basics")
my_library.show_books()

my_library.return_book("Python Basics")
my_library.show_books()
