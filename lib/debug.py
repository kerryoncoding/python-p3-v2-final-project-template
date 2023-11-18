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
   Customer.create("John", "New York", book1.id)
   Customer.create("Dave", "Philadelphia", book1.id)
   Customer.create("Mary", "Miami", book2.id)
   Customer.create("Alex", "Chicago", book3.id)
   Customer.create("Beth", "Detriot", book2.id)
   Customer.create("Brian", "Omaha", book1.id)
   Customer.create("Samantha", "Newark", book3.id)


reset_database()
ipdb.set_trace()
