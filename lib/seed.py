#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.book import Book
from models.customer import Customer

def seed_database():
    Customer.drop_table()
    Book.drop_table()
    Book.create_table()
    Customer.create_table()

    # Create seed data
    payroll = Book.create("Payroll", "Building A, 5th Floor")
    human_resources = Book.create(
        "Human Resources", "Building C, East Wing")
    Customer.create("John", 25, payroll.id)
    Customer.create("Dave", 38, payroll.id)
    Customer.create("Mary", 19, human_resources.id)
    Customer.create("Alex", 27, human_resources.id)
    Customer.create("Beth", 42, human_resources.id)


seed_database()
print("Seeded database")