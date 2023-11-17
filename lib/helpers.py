# lib/helpers.py
from models.book import Book
from models.customer import Customer

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

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

# skipping update book

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

def create_customer():
    name = input("Enter the customer's name: ")
    age = input("Enter the customer's age: ")
    book_id = input("Enter the customer's Book id:")
    try:
        customer = Customer.create(name, age, book_id)
        print(f'Success: {customer}')
    except Exception as exc:
        print("Error creating customer: ", exc)

    # skipping update customer

def delete_customer():
    id_ = input("Enter the customer's id: ")
    if customer:= Customer.find_by_id(id_):
        customer.delete()
        print(f'Customer {id_} deleted')
    else:
        print(f'Customer {id_} not found')


def list_book_customers():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        for customer in book.customers():
            print(customer)
    else:
        print(f'Customer {id_} not found')   