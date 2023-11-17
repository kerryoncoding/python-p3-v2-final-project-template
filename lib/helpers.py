# lib/helpers.py
from models.book import Book
from models.customer import Customer

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(book) if book else print(
        f'Book {title} not found')
 

def find_book_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the book's id: ")
    book = Book.find_by_id(id_)
    print(book) if book else print(f'Book {id_} not found')

def create_book():
    title = input("Enter the book's title: ")
    author= input("Enter the book's author: ")
    try:
        book = book.create(title, author)
        print(f'Success: {book}')
    except Exception as exc:
        print("Error creating book: ", exc)

