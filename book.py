class Book:
    """
    A class representing a book in a library management system.

    Attributes:
        title (str): The title of the book
        author (str): The author's name
        isbn (str): The International Standard Book Number
        pageCount (int): The total number of pages
        isCheckedOut (bool): Whether the book is currently borrowed
    """

    def __init__(self, title, author, isbn, pageCount):
        """
        Initialize a new Book instance.

        Args:
            title (str): The title of the book
            author (str): The author's name
            isbn (str): The International Standard Book Number
            pageCount (int): The total number of pages
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pageCount = pageCount
        self.isCheckedOut = False

    def checkOut(self):
        """
        Check out the book if it's available.

        Returns:
            bool: True if successfully checked out, False if already checked out
        """
        if not self.isCheckedOut:
            self.isCheckedOut = True
            return True
        return False

    def returnBook(self):
        """
        Return the book, making it available for checkout.

        Returns:
            bool: True if successfully returned, False if wasn't checked out
        """
        if self.isCheckedOut:
            self.isCheckedOut = False
            return True
        return False

    def getSummary(self):
        """
        Get a summary of the book with title, author, and ISBN.

        Returns:
            str: A formatted string with book details
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def setPageCount(self, newCount):
        """
        Update the page count (e.g., for an edition change).

        Args:
            newCount (int): The new page count

        Raises:
            ValueError: If newCount is not a positive integer
        """
        if not isinstance(newCount, int) or newCount <= 0:
            raise ValueError("Page count must be a positive integer")
        self.pageCount = newCount

    def isAvailable(self):
        """
        Check if the book is available for checkout.

        Returns:
            bool: True if available, False if checked out
        """
        return not self.isCheckedOut

    def __str__(self):
        """
        String representation of the book.

        Returns:
            str: A formatted string representation
        """
        status = "Available" if self.isAvailable() else "Checked Out"
        return f"{self.title} by {self.author} ({self.isbn}) - {self.pageCount} pages - {status}"

    def __repr__(self):
        """
        Official string representation of the book.

        Returns:
            str: A string that could recreate the object
        """
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.pageCount})"


# Example usage and testing
if __name__ == "__main__":
    # Create a book instance
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", 180)

    print("Initial book state:")
    print(book)
    print(f"Summary: {book.getSummary()}")
    print(f"Available: {book.isAvailable()}")

    # Check out the book
    print("\nChecking out the book...")
    success = book.checkOut()
    print(f"Checkout successful: {success}")
    print(f"Available: {book.isAvailable()}")
    print(book)

    # Try to check out again
    print("\nTrying to check out again...")
    success = book.checkOut()
    print(f"Checkout successful: {success}")

    # Return the book
    print("\nReturning the book...")
    success = book.returnBook()
    print(f"Return successful: {success}")
    print(f"Available: {book.isAvailable()}")
    print(book)

    # Update page count
    print("\nUpdating page count...")
    book.setPageCount(200)
    print(f"New page count: {book.pageCount}")
    print(book)
