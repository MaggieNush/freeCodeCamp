"""
Problem 5: Library Book Management System
A more complex system with nested data!
Requirements:
Each book is stored as: book_id: {"title": "...", "author": "...", "available": True/False}

add_book(library, book_id, title, author)
    Store book with available: True by default
    Book ID should be uppercase
"""     

def add_book(library, book_id, title, author):
    book_id = book_id.upper()
    
    if book_id in library:
        return f"Book {book_id} already exists"
    
    book_info = {
        "title": title,
        "author": author,
        "available": True
    }

    # Storing book id into book info
    library[book_id] = book_info
    
    
    return f"{book_id} added successfully!"


"""
checkout_book(library, book_id)
    If book exists and available: set available: False, return success
    If book exists but not available: return "Book is already checked out!"
    If book doesn't exist: return error
"""
def checkout_book(library, book_id):
    # Convert book id to uppercase
    book_id = book_id.upper()

    if book_id not in library:
        return "Book not found!"
    if library[book_id]["available"] == False:
        return f"{book_id} is already checked out!"
    else:
        library[book_id]["available"] = False 
        return f"{book_id} is checked out successfully!"

"""
return_book(library, book_id)
    Set available: True
"""
def return_book(library, book_id):
    book_id = book_id.upper()

    if book_id not in library:
        return "Book not found!"
    if library[book_id]["available"] == True:
        return f"Book {book_id} is already returned!"
    else:
        library[book_id]["available"] = True
        return f"Book {book_id} is returned successfully!"


"""
search_by_author(library, author_name) - NEW CHALLENGE!
    Return list of all books by this author
    Format each as: "[book_id]: [title]"
"""
def search_by_author(library, author_name):
    """Find all books by a specific author"""
    if not library:
        return "No books in the library."
    
    author_books = []
    for book_id, book_info in library.items():
        if book_info["author"].lower() == author_name.lower():
            author_books.append(f"{book_id}: {book_info['title']}")
    
    if not author_books:
        return f"No books found by {author_name}."
    
    result = f"Books by {author_name}:\n"
    for book in author_books:
        result += f"{book}\n"
    return result

"""
view_available_books(library) - show only available books
"""
def view_available_books(library):
    if not library:
        return "Book not found!"
    
    available_books = []
    for book_id, book_info in library.items():
        if book_info["available"] == True:
            available_books.append(f"{book_id}: {book_info["title"]} by {book_info["author"]}")
    if not available_books:
        return "No books currently available"
    
    result = "Available Books:\n"
    for book in available_books:
        result += f"{book}\n"
    return result


library = {}

print("=== Adding Books ===")
print(add_book(library, "bk001", "Things Fall Apart", "Chinua Achebe"))
print(add_book(library, "BK002", "Weep Not Child", "Ngugi wa Thiong'o"))
print(add_book(library, "bk003", "No Longer at Ease", "Chinua Achebe"))
print(add_book(library, "BK001", "Duplicate", "Author"))

print("\n=== View All Available Books ===")
print(view_available_books(library))

print("=== Checkout Books ===")
print(checkout_book(library, "bk001"))  
print(checkout_book(library, "BK002"))  
print(checkout_book(library, "bk001"))  

print("\n=== View Available Books After Checkout ===")
print(view_available_books(library))

print("=== Return Books ===")
print(return_book(library, "BK001"))  
print(return_book(library, "bk001"))  
print("\n=== View Available Books After Return ===")
print(view_available_books(library))

print("=== Search by Author ===")
print(search_by_author(library, "Chinua Achebe"))
print(search_by_author(library, "ngugi wa thiong'o"))
print(search_by_author(library, "Unknown Author"))

print("\n=== Final Library Status ===")
print("\nAll Books in Library:")
for book_id, book_info in library.items():
    status = "Available" if book_info["available"] else "Checked Out"
    print(f"{book_id}: {book_info['title']} by {book_info['author']} - {status}")


