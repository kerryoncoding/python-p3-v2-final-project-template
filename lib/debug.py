#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.book import Book
from models.customer import Customer
import ipdb


def reset_database():
   Customer.drop_table()
   Book.drop_table()
   Book.create_table()
   Customer.create_table()

   # Create seed data

   #  what is customer_id used for?
   book1 = Book.create("The Hobbit", "JRR Tolkin")
   book2 = Book.create("Dracula", "Bram Stoker")
   book3 = Book.create("Alice in Wonderland", "Lewis Carroll")
   Customer.create("John", 25, book1.id)
   Customer.create("Dave", 38, book1.id)
   Customer.create("Mary", 19, book2.id)
   Customer.create("Alex", 27, book3.id)
   Customer.create("Beth", 42, book2.id)
   Customer.create("Brian", 53, book1.id)
   Customer.create("Samantha", 20, book3.id)


reset_database()
ipdb.set_trace()
