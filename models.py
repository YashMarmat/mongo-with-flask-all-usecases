class Author:
    def __init__(self, name: str, books_written: int):
        self.name = name
        self.books_written = books_written

class Book:
    def __init__(self, title: str, description: str, published_date, author: Author):
        self.title = title
        self.description = description
        self.published_date = published_date
        self.author = author