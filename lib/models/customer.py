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
   
   @property
   def name(self):
      return self._name
   
   @name.setter
   def name(self, name):
      if isinstance(name, str) and len(name):
         self._name = name
      else:
         raise ValueError("Name must be a non-empty string")

   @property
   def age(self):
      return self._age
   
   @age.setter
   def age(self, age):
      if isinstance(age, int) and age < 110:
         self._age = age
      else:
         raise ValueError("Age must be an integer under 110")

