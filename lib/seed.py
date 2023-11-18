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

    book1 = Book.create("The Hobbit", "JRR Tolkin")
    book2 = Book.create("Dracula", "Bram Stoker")
    book3 = Book.create("Alice in Wonderland", "Lewis Carroll")
    Customer.create("John", "Smith", book1.id)
    Customer.create("Dave", "Ollinger", book1.id)
    Customer.create("Mary", "Rosettie", book2.id)
    Customer.create("Alex", "Berks", book3.id)
    Customer.create("Beth", "Johnson", book2.id)
    Customer.create("Brian", "Washington", book1.id)
    Customer.create("Samantha", "Osborne", book3.id)


seed_database()
print("Seeded database")