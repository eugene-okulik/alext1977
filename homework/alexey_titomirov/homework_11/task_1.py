class Book:
    material_page = 'бумага'
    has_text = True

    def __init__(self, title, author, page_count, isbn, is_reserved):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved


class SchoolBook(Book):

    def __init__(self, title, author, page_count, isbn, is_reserved, subject, group, has_task):
        super().__init__(title, author, page_count, isbn, is_reserved)
        self.subject = subject
        self.group = group
        self.has_task = has_task


book_1 = Book('Война и мир', 'Толстой', 800, '123456-78', False)
book_2 = Book('Идиот', 'Достоевский', 757, '223456-21', False)
book_3 = Book('Рассказы', 'Чехов', 192, '423456-43', False)
book_4 = Book('Гамлет', 'Шекспир', 508, '623456-02', False)
book_5 = Book('Ревизор', 'Гоголь', 411, '553456-80', False)

book_4.is_reserved = True

books = [book_1, book_2, book_3, book_4, book_5]

for book in books:
    if book.is_reserved:
        reserve = ', зарезервирована'
    else:
        reserve = ''
    print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_count}, материал: {book.material_page}'
          + reserve)

school_book_1 = SchoolBook('Алгебра', 'Иванов', 280, '9876543-21',
                           False, 'Математика', 5, True)
school_book_2 = SchoolBook('Новейшая история', 'Петров', 356, '0876543-30',
                           False, 'История', 9, False)
school_book_3 = SchoolBook('Ботаника', 'Сидоров', 405, '1876543-19',
                           False, 'Биология', 7, True)

school_book_2.is_reserved = True

school_books = [school_book_1, school_book_2, school_book_3]

for s_book in school_books:
    if s_book.is_reserved:
        reserve = ', зарезервирована'
    else:
        reserve = ''
    print(f'Название: {s_book.title}, Автор: {s_book.author}, страниц: {s_book.page_count}, предмет: {s_book.subject},'
          f' класс: {s_book.group}' + reserve)
