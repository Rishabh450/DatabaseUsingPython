from utils import database

USER_CHOICE = "Enter a to add book\n Enter l to get book list\n Enter r to mark a book read\n Enter d to delete a " \
              "book\n Enter q to quit "


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown Command. Please Try again !")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter book')
    author = input('Enter Author')

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()

    for book in books:
        print(book)


def prompt_read_book():
    name = input('Enter book name that is read')
    database.mark_book_read(name)


def prompt_delete_book():
    name = input('Enter book name to delete')
    database.delete_book(name)


menu()
