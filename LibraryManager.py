# LibraryManager.py

class LibraryManager:
    def __init__(self):
        """Initialize the library with an empty book collection."""
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        """Add a book to the library."""
        if isbn in self.books:
            print("Error: Book with this ISBN already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year
            }
            print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN '{isbn}' removed successfully.")
        else:
            print("Error: Book with this ISBN does not exist.")

    def get_book_details(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print("Error: Book with this ISBN does not exist.")
            return None

    def search_books(self, query):
        """Search for books by title or author."""
        result = [book for book in self.books.values() if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
        return result

    def list_all_books(self):
        """List all books currently in the library."""
        return list(self.books.values())

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        """Update the details of an existing book."""
        if isbn in self.books:
            book = self.books[isbn]
            if title is not None:
                book['title'] = title
            if author is not None:
                book['author'] = author
            if publisher is not None:
                book['publisher'] = publisher
            if volume is not None:
                book['volume'] = volume
            if year is not None:
                book['year'] = year
            print(f"Book with ISBN '{isbn}' updated successfully.")
        else:
            print("Error: Book with this ISBN does not exist.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books

def main():
    manager = LibraryManager()

    while True:
        print("\nLibrary Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Get Book Details")
        print("4. Search Books")
        print("5. List All Books")
        print("6. Update a Book")
        print("7. Check Book Availability")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            publisher = input("Enter Publisher: ")
            volume = input("Enter Volume: ")
            year = input("Enter Year: ")
            manager.add_book(isbn, title, author, publisher, volume, year)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            manager.remove_book(isbn)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to retrieve: ")
            details = manager.get_book_details(isbn)
            if details:
                print("Book Details:", details)

        elif choice == '4':
            query = input("Enter title or author to search: ")
            results = manager.search_books(query)
            if results:
                print("Search Results:")
                for book in results:
                    print(book)
            else:
                print("No books found.")

        elif choice == '5':
            books = manager.list_all_books()
            if books:
                print("All Books:")
                for book in books:
                    print(book)
            else:
                print("No books in the library.")

        elif choice == '6':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new Title (or press Enter to skip): ")
            author = input("Enter new Author (or press Enter to skip): ")
            publisher = input("Enter new Publisher (or press Enter to skip): ")
            volume = input("Enter new Volume (or press Enter to skip): ")
            year = input("Enter new Year (or press Enter to skip): ")
            manager.update_book(isbn, title or None, author or None, publisher or None, volume or None, year or None)

        elif choice == '7':
            isbn = input("Enter ISBN of the book to check availability: ")
            if manager.check_availability(isbn):
                print("The book is available.")
            else:
                print("The book is not available.")

        elif choice == '8':
            print("Exiting the Library Manager.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
