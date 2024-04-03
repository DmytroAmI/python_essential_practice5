class Book:
    __slots__ = ("title", "author", "genre", "year_published", "isbn")

    def __init__(self, title, author, genre, year_published, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' - {self.author}, {self.genre}"

    def update_year_published(self, new_year):
        self.year_published = new_year


book1 = Book("The Shining", "King", "horror", 1978, "0112235435")
print(book1)
print("ISBN -", book1.isbn)

print("Year published -", book1.year_published)
book1.update_year_published(1979)
print("Update year published -", book1.year_published)
