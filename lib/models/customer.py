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

   @classmethod
   def create_table(cls):
      """ Create a new table to persist the attributes of Customer instances """
      sql = """
         CREATE TABLE IF NOT EXISTS customers (
         id INTEGER PRIMARY KEY,
         name TEXT,
         age INTEGER,
         FOREIGN KEY (bookeshop_id) REFERENCES bookshop(id))
      """
      CURSOR.execute(sql)
      CONN.commit()

   @classmethod
   def drop_table(cls):
      """ Drop the table that persists Customer instances """
      sql = """
         DROP TABLE IF EXISTS customers;
      """
      CURSOR.execute(sql)
      CONN.commit()
   
   def save(self):
      """ Insert a new row with the name, and age of the current Customer object.
      Update object id attribute using the primary key value of new row.
      Save the object in local dictionary using table row's PK as dictionary key"""
      sql = """
               INSERT INTO customers (name, age)
               VALUES (?, ?)
      """

      CURSOR.execute(sql, (self.name, self.age))
      CONN.commit()

      self.id = CURSOR.lastrowid
      type(self).all[self.id] = self

   def delete(self):
      """Delete the table row corresponding to the current Customer instance,
      delete the dictionary entry, and reassign id attribute"""

      sql = """
         DELETE FROM customers
         WHERE id = ?
      """

      CURSOR.execute(sql, (self.id,))
      CONN.commit()

      # Delete the dictionary entry using id as the key
      del type(self).all[self.id]

      # Set the id to None
      self.id = None