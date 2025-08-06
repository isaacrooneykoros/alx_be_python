import sys
from robust_division_calculator import safe_divide
from library_management import Book, Library

def division_mode(args):
    if len(args) != 2:
        print("Usage: python main.py division <numerator> <denominator>")
        return

    numerator = args[0]
    denominator = args[1]
    result = safe_divide(numerator, denominator)
    print(result)

def library_mode():
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py division <numerator> <denominator>")
        print("  python main.py library")
        sys.exit(1)

    mode = sys.argv[1]
    args = sys.argv[2:]

    if mode == "division":
        division_mode(args)
    elif mode == "library":
        library_mode()
    else:
        print("Unknown mode. Use 'division' or 'library'.")

if __name__ == "__main__":
    main()
