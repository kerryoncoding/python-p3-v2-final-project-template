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

# skipping update

def delete_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book {id_} deleted')
    else:
        print(f'Book {id_} not found')

# Customers...

def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def find_customer_by_name():
    name = input("Enter the customers's name: ")
    customer = Customer.find_by_name(name)
    print(customer) if customer else print(
        f'Customer {name} not found')
    
def find_customer_by_id():
    id_ = input("Enter the customer's id: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f'Customer {id_} not found')

