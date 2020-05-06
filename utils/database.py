books = 'books.txt'


def add_book(name, author):
    with open(books, 'a') as file:
        file.write(f'{name},{author},0\n')


def get_all_books_list():
    lines = get_all_books()
    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def mark_book_read(name):
    lines = get_all_books()
    for line in lines:
        if line[0] == name:
            line[2] = 1
    save_book_list(lines)


def get_all_books():
    with open(books, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return lines


def save_book_list(lines):
    with open(books, 'w') as files:
        for line in lines:
            files.write(f'{line[0]},{line[1]},{line[2]}\n')


def delete_book(name):
    lines = get_all_books()

    nlines = [line for line in lines if line[0] != name]

    save_book_list(nlines)

