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
    find_customer_by_name,
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
        elif choice == "1":
            list_books()
        elif choice == "2":
            find_book_by_title()
        elif choice == "3":
            find_book_by_id()
        elif choice == "4":
            create_book()
        # elif choice == "x":
        #     update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            list_customers()
        elif choice == "7":
            find_customer_by_name()
        elif choice == "8":
            find_customer_by_id()
        elif choice == "9":
            create_customer()
        # elif choice == "x":
        #     update_customer()
        elif choice == "10":
            delete_customer()
        elif choice == "11":
            list_book_customers()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all books")
    print("2. Find book by name")
    print("3. Find book by id")
    print("4: Create book")
    # print("x: Update book")
    print("5: Delete book")
    print("6. List all customers")
    print("7. Find customer by name")
    print("8. Find customer by id")
    print("9: Create customer")
    # print("x: Update customer")
    print("10: Delete customer")
    print("11: List all customers who bought book")


if __name__ == "__main__":
    main()
