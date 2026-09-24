# Library Management System
# Using functions and file handling

FILE_NAME = "books.txt"


# Function to add a book
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author_name = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(book_id + "," + book_name + "," + author_name + "\n")

    print("Book added successfully!")


# Function to view all books
def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

            if len(books) == 0:
                print("No books available.")
            else:
                print("\n----- Book Details -----")

                for book in books:
                    data = book.strip().split(",")

                    print("Book ID:", data[0])
                    print("Book Name:", data[1])
                    print("Author Name:", data[2])
                    print("------------------------")

    except FileNotFoundError:
        print("No books found.")


# Function to search a book
def search_book():
    search_id = input("Enter Book ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for book in file:
                data = book.strip().split(",")

                if data[0] == search_id:
                    print("\nBook Found!")
                    print("Book ID:", data[0])
                    print("Book Name:", data[1])
                    print("Author Name:", data[2])

                    found = True
                    break

            if not found:
                print("Book not found.")

    except FileNotFoundError:
        print("No books found.")


# Function to delete a book
def delete_book():
    delete_id = input("Enter Book ID to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for book in books:
                data = book.strip().split(",")

                if data[0] == delete_id:
                    found = True
                else:
                    file.write(book)

        if found:
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    except FileNotFoundError:
        print("No books found.")


# Main program
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")