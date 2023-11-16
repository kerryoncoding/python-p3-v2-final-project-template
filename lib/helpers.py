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
    for customer in customer:
        print(customer)