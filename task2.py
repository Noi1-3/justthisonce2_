class book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"название: {self.title}, год: {self.year}, издатель: {self.publisher}, жанр: {self.genre}, автор: {self.author}, цена: {self.price}"

    def input_data(self):
        self.title = input("введите название книги: ")
        self.year = input("введите год издания: ")
        self.publisher = input("введите издателя: ")
        self.genre = input("введите жанр: ")
        self.author = input("введите автора: ")
        self.price = input("введите цену: ")

    def update_publisher(self, new_publisher):
        self.publisher = new_publisher

my_book = book("1984", 1949, "secker & warburg", "антиутопия", "джордж оруэлл", 500)
print(my_book)