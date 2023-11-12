# lib/models/bookshop.py
from models.__init__ import CURSOR, CONN

class Bookshop:
   all = {}

   def __init__(self, title, author):
      self.id = id
      self.title = title
      self.author = author

   def __repr__(self):
      return f"<Book ID: {self.id}, Book Title: {self.title}, Author: {self.author}"
   
   @property
   def Title(self):
      return self._title
   
   @author.setter
   def author(self, title):
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