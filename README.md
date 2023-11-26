# Phase 3 CLI+ORM Project Template

This README serves as a template. Replace the contents of this file to describe the important files in your project and describe what they do. Each Python file that you edit should get at least a paragraph, and each function should be described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest should be ordered by importance to the user. (Probably functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to users and collaborators, but 
a little more syntactically complicated. Only add these in if you're feeling comfortable with Markdown.

----------------------VVVVVV here  VVVVVV

This file is for my Flatiron school phase 3 project. It implements a Python application that inlcudes a Command Line Interface.  It has Object-Relational Mapping functions for the classes of Book and Customer.  Book to Customer is a one-to-many relationship. 


## Description

This file is for my Flatiron school phase 3 project. It implements a Python application that inlcudes a Command Line Interface.  It has Object-Relational Mapping functions for the classes of Book and Customer.  Book to Customer is a one-to-many relationship. 

First run pipenv install and pipenv shell.
Seed the database with the seed.py file:  python lib/seed.py

Enter the Command Line Interface: python lib/cli.py

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
    


## Introduction

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
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---




---------^^^^^^^^^^^^ here




## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---



### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
