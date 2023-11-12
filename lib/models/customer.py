# lib/models/customer.py
from models.__init__ import CURSOR, CONN
from models.bookshop import Bookshop

class Customer:
   all = {}

   def __init__(self, name, age, id=None):
      self.id = id
      self.name = name
      self.age = age

   def __repr__(self):
      return(f"<Customer ID: {self.id}, Name: {self.name}, age: {self.age}")
   