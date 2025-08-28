from book import Book


library = [
    Book("Война и мир", "Лев Николаевич Толстой"),
    Book("Евгений Онегин", "Александр Сергеевич Пушкин"),
    Book("Отцы и дети", "Иван Сергеевич Тургенев")
]


for book in library:
    print(f"{book.nameBook} - {book.authorBook}")