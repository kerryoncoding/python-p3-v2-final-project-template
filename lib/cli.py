# lib/cli.py

from helpers import (
    exit_program,
    list_books,
    find_book_by_title,
    find_book_by_id,
    create_book,
    # update_book,
    delete_book,
    list_customers,
    find_customer_by_firstname,
    find_customer_by_lastname,
    find_customer_by_id,
    create_customer,
    # update_customer,
    delete_customer,
    list_book_customers
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        # elif choice == "1":
        #     list_books()
        # elif choice == "2":
        #     find_book_by_title()
        # elif choice == "3":
        #     find_book_by_id()
        elif choice == "1":
            create_book()
        # elif choice == "x":
        #     update_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            list_customers()
        elif choice == "4":
            find_customer_by_firstname()
        elif choice == "5":
            find_customer_by_lastname()
        elif choice == "6":
            find_customer_by_id()
        elif choice == "7":
            create_customer()
        # elif choice == "x":``
        #     update_customer()
        elif choice == "8":
            delete_customer()
        elif choice == "9":
            list_book_customers()
        else:
            print("Invalid choice")


def menu():
    print(f'\n*** Available books on sale ***')
    list_books()
    print(f'*******************************\n')
    print("Please select an option:")
    print("0. Exit the program")
    # print("1. List books for sale")
    # print("2. Find book by title")
    # print("3. Find book by id")
    print("1: Add book to on sale list")
    # print("x: Update book")
    print("2: Delete book")
    print("3. List all customers")
    print("4. Find customer by firstname")
    print("5. Find customer by firstname")
    print("6. Find customer by id")
    print("7: Create customer")
    # print("x: Update customer")
    print("8: Delete customer")
    print("9: List all customers who bought book")


if __name__ == "__main__":
    main()
