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

   #  what is customer_id used for?
    nyc = Book.create("Strand", "New York")
    philly = Book.create(
        "Blue Marble", "Philadelphia")
    Customer.create("John", 25, nyc.id)
    Customer.create("Dave", 38, nyc.id)
    Customer.create("Mary", 19, philly.id)
    Customer.create("Alex", 27, philly.id)
    Customer.create("Beth", 42, philly.id)


seed_database()
print("Seeded database")