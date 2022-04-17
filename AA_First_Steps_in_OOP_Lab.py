# 01. Rhombus of Stars
# def rhombus_of_starts(_max_stars: int):
#     _first_direction = 1
#
#     def print_line_of_starts(_counter, _direction):
#         if _counter == 0:
#             return
#         line = ' ' * (_max_stars - _counter) + '* ' * _counter
#         print(line.rstrip())
#
#         if _counter == _max_stars:
#             _direction = -1
#
#         print_line_of_starts(_counter + _direction, _direction)
#
#     return print_line_of_starts(1, _first_direction)
#
#
# rhombus_of_starts(int(input()))

# 02. Scope Mess
# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         global x
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
#
# print(x)
# outer()
# print(x)

# 03. Class Book
# class Book:
#     def __init__(self, name: str, author: str, pages: int):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#
# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)

# 04. Car
# class Car:
#
#     def __init__(self, name: str, model: str, engine: str):
#         self.engine = engine
#         self.model = model
#         self.name = name
#
#     def get_info(self):
#         return f"This is {self.name} {self.model} with engine {self.engine}"
#
#
# car = Car("Kia", "Rio", "1.3L B3 I4")
# print(car.get_info())

# 05. Music
# class Music:
#     def __init__(self, title: str, artist: str, lyrics: str):
#         self.title = title
#         self.artist = artist
#         self.lyrics = lyrics
#
#     def print_info(self):
#         return f'This is "{self.title}" from "{self.artist}"'
#
#     def play(self):
#         return self.lyrics
#
#
# song = Music("Title", "Artist", "Lyrics")
# print(song.print_info())
# print(song.play())
