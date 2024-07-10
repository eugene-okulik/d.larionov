class Book:

    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, name_book, author, count_page, isbn, reserved):
        self.name_book = name_book
        self.author = author
        self.count_page = count_page
        self.isbn = isbn
        self.reserved = reserved

    def print_book(self):
        if self.reserved is True:
            print(
                'Название: {}, Автор: {}, Количество страниц: {}, Материал страниц: {}, Зарезервирована '
                .format(self.name_book, self.author, self.count_page, self.page_material)
    )
        else:
            print(
                'Название: {}, Автор: {}, Количество страниц: {}, Материал страниц: {}'
                .format(self.name_book, self.author, self.count_page, self.page_material)
    )


class SchoolBook(Book):

    def __init__(self, name_book, author, count_page, isbn, reserved, lesson_subj, number_class, task):
        super().__init__(name_book, author, count_page, isbn, reserved)
        self.lesson_subj = lesson_subj
        self.number_class = number_class
        self.task = task

    def print_schoo_book(self):
        if self.task is True:
            print(
                'Название: {}, Автор: {}, Страниц: {}, Предмет: {}, Класс: {}, Зарезервирована'
                .format(self.name_book, self.author, self.count_page, self.lesson_subj, self.number_class)
    )
        else:
            print(
                'Название: {}, Автор: {}, Страниц: {}, Предмет: {}, Класс: {}'
                .format(self.name_book, self.author, self.count_page, self.lesson_subj, self.number_class)
    )


book1 = Book('Идиот', 'Достоевский', 500, 222222, True)
book2 = Book('Идиот', 'Достоевский', 500, 222555, False)
book3 = Book('Мысль', 'Чехов', 700, 222555, False)
school_book1 = SchoolBook('Алгебра', 'Иванов', 250, 222299999, True, 'Математика', 9, True)
school_book2 = SchoolBook('Геометрия', 'Бантова', 259, 22229775, True, 'Геометрия', 9, False)
school_book3 = SchoolBook('Природоведение', 'Сонин', 259, 55557777, True, 'Природоведение', 9, False)
school_book1.print_schoo_book()
school_book2.print_schoo_book()
school_book3.print_schoo_book()
book1.print_book()
book2.print_book()
book3.print_book()
