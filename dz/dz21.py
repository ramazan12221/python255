class Book:
    name_book = "name"
    year_of_release = '00.00.00'
    publisher = 'publisher'
    genre = 'genre'
    author = 'author'
    price = '$'

    def print_info(self):
        print(' КНИГА '.center(40, '*'))
        print(f'НАЗВАНИЕ: {self.name_book}\nДата выпуска: {self.year_of_release}\n'
              f'Издательство:{self.publisher}\n Жанр: {self.genre}\n'
              f'Автор: {self.author}\n Цена: {self.price}')
        print('=' * 40)

    def input_info(self, name_book, year_of_release, publisher, genre, author, price):
        self.name_book = name_book
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name_book):
        self.name_book = name_book

    def get_name(self):
        return self.name_book

    def set_year(self, year_of_release):
        self.year_of_release = year_of_release

    def get_year(self):
        return self.year_of_release

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


h1 = Book()
h1.input_info('Дети капитана Гранта', "1865", "Пьер-Жюль Этцель", 'Приключенческий Роман',
              "Жюль Верн", "500 руб")
h1.print_info()
h1.set_name("Хоббит")
h1.set_year("1937")
h1.set_publisher("George Allen & Unwin")
h1.set_genre("детская литература, сказка, фэнтези")
h1.set_author("Джон Р. Р. Толкин")
h1.set_price("500 руб")
print(h1.get_name())
print(h1.get_year())
print(h1.get_publisher())
print(h1.get_genre())
print(h1.get_author())
print(h1.get_price())
