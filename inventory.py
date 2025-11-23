from book import Book

class LibraryInventory:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    if line.strip():
                        self.books.append(Book.from_line(line))
        except FileNotFoundError:
            open(self.file_name, "w").close()  # create empty file

    def save_books(self):
        with open(self.file_name, "w") as f:
            for b in self.books:
                f.write(b.to_line())

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        for b in self.books:
            print(b)
