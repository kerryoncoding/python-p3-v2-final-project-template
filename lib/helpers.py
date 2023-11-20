# lib/helpers.py
from models.book import Book
from models.customer import Customer

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print(f"Goodbye!\n")
    exit()

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def find_book_by_title():
    title = input(f'\nEnter the book\'s title: ')
    book = Book.find_by_title(title)
    print(f'\n{book}') if book else print(f'\nBook title: "{title}" not found')
 

# def find_book_by_id():
#     # use a trailing underscore not to override the built-in id function
#     id_ = input(f"\nEnter the book's id: ")
#     book = Book.find_by_id(id_)
#     print(f'\n{book}') if book else print(f'\nBook ID: {id_} not found')

def create_book():
    title = input(f"\nEnter the book's title: ")
    author= input("Enter the book's author: ")
    try:
        book = Book.create(title, author)
        print(f'\nSuccess: {book}')
    except Exception as exc:
        print("Error creating book: ", exc)

# skipping update book

def delete_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        # also get's rid of any customer who owns that book
        for customer in book.customers():
            customer.delete()
        # gets rid of book with that ID
        book.delete()
        print(f'\nBook {id_} deleted\n')
        # also get's rid of any customer who owns that book
        # for customer in book.customers():
        #     customer.delete()
        # if customer:= Customer.find_by_id(book.id_):
        #     customer.delete()
        #     print(f'\nCustomer {id_} deleted')

    else:
        print(f'\nBook ID: {id_} not found')

# Customers...

def list_customers():
    customers = Customer.get_all()
    print(f'\n')
    for customer in customers:
        print(customer)

def find_customer_by_firstname():
    firstname = input(f'\nEnter the customer\'s firstname: \n')
    customer = Customer.find_by_firstname(firstname)
    print(customer) if customer else print(f'\nCustomer firstname: "{firstname}" not found')

def find_customer_by_lastname():
    lastname = input(f'\nEnter the customer\'s lastname: \n')
    customer = Customer.find_by_lastname(lastname)
    print(customer) if customer else print(f'\nCustomer lastname: "{lastname}" not found')
    
def find_customer_by_id():
    id_ = input(f'\nEnter the customer\'s id: \n')
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f'\nCustomer ID: {id_} not found')

def create_customer():
    firstname = input(f'\nEnter the customer\'s firstname: ')
    lastname= input("Enter the customer's lastname: ")
    book_id = input("Enter the customer's purchased Book id: ")
    try:
        customer = Customer.create(firstname, lastname, int(book_id))
        print(f'\nSuccess: {customer}')
    except Exception as exc:
        print(f'\nError creating customer: ', exc)

    # skipping update customer

def delete_customer():
    id_ = input(f'\nEnter the customer\'s id: \n')
    if customer:= Customer.find_by_id(id_):
        customer.delete()
        print(f'\nCustomer {id_} deleted')
    else:
        print(f'\nCustomer ID: {id_} not found')


def list_book_customers():
    id_ = input(f'\nEnter the book\'s id: \n')
    if book := Book.find_by_id(id_):
        for customer in book.customers():
            print(customer)
    else:
        print(f'\nBook ID: {id_} not found')   