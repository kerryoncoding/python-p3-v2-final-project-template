# lib/models/customer.py
from models.__init__ import CURSOR, CONN
from models.book import Book

class Customer:
   all = {}

   def __init__(self, name, age, book_id, id=None):
      self.id = id
      self.name = name
      self.age = age
      self.book_id = book_id

   def __repr__(self):
      return(f"<Customer: {self.id}, Name: {self.name}, age: {self.age} " + f"Book ID: {self.book_id}>")
   
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

   @property
   def book_id(self):
        return self._book_id

   @book_id.setter
   def book_id(self, book_id):
      if type(book_id) is int and Book.find_by_id(book_id):
         self._book_id = book_id
      else:
         raise ValueError("book_id must reference a book in the database")

   @classmethod
   def create_table(cls):
      """ Create a new table to persist the attributes of Customer instances """
      sql = """
         CREATE TABLE IF NOT EXISTS customers (
         id INTEGER PRIMARY KEY,
         name TEXT,
         age INTEGER,
         book_id INTEGER,
         FOREIGN KEY (book_id) REFERENCES book(id))
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
               INSERT INTO customers (name, age, book_id)
               VALUES (?, ?, ?)
      """

      CURSOR.execute(sql, (self.name, self.age, self.book_id))
      CONN.commit()

      self.id = CURSOR.lastrowid
      type(self).all[self.id] = self

# skipped update

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

   @classmethod
   def create(cls, name, age, book_id):
      """ Initialize a new Customer instance and save the object to the database """
      customer = cls(name, age, book_id)
      customer.save()
      return customer
   
   @classmethod
   def instance_from_db(cls, row):
      """Return a Customer object having the attribute values from the table row."""

      # Check the dictionary for  existing instance using the row's primary key
      customer = cls.all.get(row[0])
      if customer:
         # ensure attributes match row values in case local instance was modified
         customer.name = row[1]
         customer.age = row[2]
         customer.book_id = [3]
      else:
         # not in dictionary, create new instance and add to dictionary
         customer = cls(row[1], row[2], row[3])
         customer.id = row[0]
         cls.all[customer.id] = customer
      return customer
   
   @classmethod
   def get_all(cls):
      """Return a list containing one Customer object per table row"""
      sql = """
         SELECT *
         FROM customers
      """

      rows = CURSOR.execute(sql).fetchall()

      return [cls.instance_from_db(row) for row in rows]

   @classmethod
   def find_by_id(cls, id):
      """Return Customer object corresponding to the table row matching the specified primary key"""
      sql = """
         SELECT *
         FROM customers
         WHERE id = ?
      """

      row = CURSOR.execute(sql, (id,)).fetchone()
      return cls.instance_from_db(row) if row else None   
   
   @classmethod
   def find_by_name(cls, name):
      """Return Customer object corresponding to first table row matching specified name"""
      sql = """
         SELECT *
         FROM customer
         WHERE name is ?
      """

      row = CURSOR.execute(sql, (name,)).fetchone()
      return cls.instance_from_db(row) if row else None
   

  