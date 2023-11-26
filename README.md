# Phase 3 CLI+ORM Project Template


## Description

This file is for my Flatiron school phase 3 project. It implements a Python application that inlcudes a Command Line Interface.  It has Object-Relational Mapping functions for the classes of Book and Customer.  Book to Customer is a one-to-many relationship. 

First install Pipfile if not already done:
    Run in console: pipenv install
    Run in console: pipenv shell

Seed the database with the seed.py file:
    Run in console: python lib/seed.py

Enter the Command Line Interface: 
    Run in console: python lib/cli.py

The current list of available books on-sale will be displayed followed by the following options:

    0. Exit the program
        this will exit you out of the command line interface
    1. List books for sale
        this will list the current Available books on-sale
    2. Find book by title
        The user will be prompted to enter a title.  
        If the title exists in the list of available books, then that book object will be displayed.  If it does not match, it will say that it is not found.
    3. Find book by id
        The user will be prompted to enter an id
        If the id exists in the list of available books, then that book object will be displayed.  If it does not exist, it will say that it is not found.
    4. Add book to on-sale list
        The user will be prompted to enter the book Title. 
        The user will be prompted to enter the book Author.
        Both entries for Title and Author must be non-empty strings or an error will show and book object will not be created.
        Prompt will say if book object is successfully created.  This adds book to the Available books on-sale list and will display above the options.
    5. Delete book from on-sale list
        The user will be prompted to enter book id.
        If the id exists in the list of available books, then that book object will be deleted.  If it does not exist, it will say that it is not found.
        In addition, any customers who purchased that book will be removed from the customer list.
    6. List all customers
        This will list customers who have purchased the current Available books on-sale
    7. Find customer by firstname
        The user will be promoted to enter the customer's firstname.
        If the firstname matches with a customer's firstname it will return the first customer object that matches. If it does not match, it will say that it is not found.  Firstname must be a non-empty string or it will return an error.
    8. Find customer by lastname
        The user will be promoted to enter the customer's lastname.
        If the lastname matches with a customer's lasttname it will return the first customer object that matches. If it does not match, it will say that it is not found.  Lastname must be a non-empty string or it will return an error.
    9. Find customer by id
        The user will be prompted to enter an id
        If the id exists in the list of customers, then that customer object will be displayed.  If it does not exist, it will say that it is not found.
    10. Create customer
        User will be prompted to enter the customer's firstname.
        User will be prompted to enter the customer's lastname.
        User will be prompted to enter the book id that the customer purchased.
        Both entries for firstname and lastnem must be non-empty strings.  Also the book id must exist in the list of book objects or an error will show and customer object will not be created.
        Prompt will say if customer object is successfully created.  This adds a customer object to the list of customers.
    11. Delete customer
        The user will be prompted to enter customer id.
        If the id exists in the list of customers, then that customer object will be deleted.  If it does not exist, it will say that it is not found.
    12. List all customers who bought book
        The user will be prompted to enter a book id.
        If the book id exists in the list of available books on-sale, the list will display all customers who purchased that book.
        Otherwise prompt will say id is not found.
    

## File Structure

This is the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── book.py
    |   └── customer.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard these files.

---



