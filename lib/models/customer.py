# lib/models/customer.py
from models.__init__ import CURSOR, CONN
from models.book import Book

class Customer:
   all = {}

   def __init__(self, firstname, city, book_id, id=None):
      self.id = id
      self.firstname = firstname
      self.city = city
      self.book_id = book_id

   def __repr__(self):
      return(
         f"<Customer ID: {self.id}, Name: {self.firstname}, city: {self.city}, " + 
         f"Book ID: {self.book_id}>"
         )
   
   @property
   def firstname(self):
      return self._name
   
   @firstname.setter
   def firstname(self, firstname):
      if isinstance(firstname, str) and len(firstname):
         self._name = firstname
      else:
         raise ValueError("Name must be a non-empty string")

   @property
   def city(self):
      return self._city
   
   @city.setter
   def city(self, city):
      if isinstance(city, str) and len(city) > 0:
         self._city = city
      else:
         raise ValueError("City must be a non-empty string")

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
         firstname TEXT,
         city TEXT,
         book_id INTEGER,
         FOREIGN KEY (book_id) REFERENCES books(id))
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
      """ Insert a new row with the firstname, city, and book id  values of the current Customer object.
      Update object id attribute using the primary key value of new row.
      Save the object in local dictionary using table row's PK as dictionary key"""
      sql = """
               INSERT INTO customers (firstname, city, book_id)
               VALUES (?, ?, ?)
      """

      CURSOR.execute(sql, (self.firstname, self.city, self.book_id))
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
   def create(cls, firstname, city, book_id):
      """ Initialize a new Customer instance and save the object to the database """
      customer = cls(firstname, city, book_id)
      customer.save()
      return customer
   
   @classmethod
   def instance_from_db(cls, row):
      """Return a Customer object having the attribute values from the table row."""

      # Check the dictionary for  existing instance using the row's primary key
      customer = cls.all.get(row[0])
      if customer:
         # ensure attributes match row values in case local instance was modified
         customer.firstname = row[1]
         customer.city = row[2]
         customer.book_id = row[3]
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
   def find_by_name(cls, firstname):
      """Return Customer object corresponding to first table row matching specified firstname"""
      sql = """
         SELECT *
         FROM customers
         WHERE firstname is ?
      """
      row = CURSOR.execute(sql, (firstname,)).fetchone()
      return cls.instance_from_db(row) if row else None
   

  