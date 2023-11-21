# lib/models/book.py
from models.__init__ import CURSOR, CONN

class Book:
   all = {}

   def __init__(self, title, author, id=None):
      self.id = id
      self.title = title
      self.author = author

   def __repr__(self):
      return f"<Book ID: {self.id}, Book Title: {self.title}, Author: {self.author}>"
   
   @property
   def title(self):
      return self._title
   
   @title.setter
   def title(self, title):
      if isinstance(title, str) and len(title):
         self._title = title
      else:
         raise ValueError("Title must be a non-empty string")

   @property
   def author(self):
      return self._author
   
   @author.setter
   def author(self, author):
      if isinstance(author, str) and len(author):
         self._author = author
      else:
         raise ValueError("Author must be a non-empty string")
      
   @classmethod
   def create_table(cls):
      """ Create a new table to persist the attributes of Book instances """
      sql = """
         CREATE TABLE IF NOT EXISTS books (
         id INTEGER PRIMARY KEY,
         title TEXT,
         author TEXT)
      """
      CURSOR.execute(sql)
      CONN.commit()

   @classmethod
   def drop_table(cls):
      """ Drop the table that persists Book instances """
      sql = """
         DROP TABLE IF EXISTS books;
      """
      CURSOR.execute(sql)
      CONN.commit()

   def save(self):
      """ Insert a new row with the title and author values of the current Book instance.
      Update object id attribute using the primary key value of new row.
      Save the object in local dictionary using table row's PK as dictionary key"""
      sql = """
         INSERT INTO books (title, author)
         VALUES (?, ?)
      """

      CURSOR.execute(sql, (self.title, self.author))
      CONN.commit()

      self.id = CURSOR.lastrowid
      type(self).all[self.id] = self

   @classmethod
   def create(cls, title, author):
      """ Initialize a new Book instance and save the object to the database """
      book = cls(title, author)
      book.save()
      return book    

   def delete(self):
      """Delete the table row corresponding to the current Book instance,
      delete the dictionary entry, and reassign id attribute"""

      sql = """
         DELETE FROM books
         WHERE id = ?
      """

      CURSOR.execute(sql, (self.id,))
      CONN.commit()

      del type(self).all[self.id]
      self.id = None

   @classmethod
   def instance_from_db(cls, row):
      """Return a Book object having the attribute values from the table row."""

      book = cls.all.get(row[0])
      if book:
         book.title = row[1]
         book.author = row[2]
      else:
         book = cls(row[1], row[2])
         book.id = row[0]
         cls.all[book.id] = book
      return book
   
   @classmethod
   def get_all(cls):
      """Return a list containing a Book object per row in the table"""
      sql = """
         SELECT *
         FROM books
      """

      rows = CURSOR.execute(sql).fetchall()

      return [cls.instance_from_db(row) for row in rows]
   
   @classmethod
   def find_by_id(cls, id):
      """Return a Book object corresponding to the table row matching the specified primary key"""
      sql = """
         SELECT *
         FROM books
         WHERE id = ?
      """

      row = CURSOR.execute(sql, (id,)).fetchone()
      return cls.instance_from_db(row) if row else None


   @classmethod
   def find_by_title(cls, title):
      """Return a Book object corresponding to first table row matching specified title"""
      sql = """
         SELECT *
         FROM books
         WHERE title is ?
      """

      row = CURSOR.execute(sql, (title,)).fetchone()
      return cls.instance_from_db(row) if row else None
   
   def customers(self):
      """Return list of customers associated with current book"""
      from models.customer import Customer
      sql = """
         SELECT * FROM customers
         WHERE book_id = ?
      """
      CURSOR.execute(sql, (self.id,),)

      rows = CURSOR.fetchall()
      return [Customer.instance_from_db(row) for row in rows]