# 01. Custom Range
# class custom_range:
#
#     def __init__(self, start, end):
#         self.end = end
#         self.start = start
#         self.counter = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.counter
#         if value > self.end:
#             raise StopIteration
#         self.counter += 1
#         return value

# 02. Reverse Iter
# class reverse_iter:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.__index = len(self.iterable) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__index < 0:
#             raise StopIteration
#         value = self.iterable[self.__index]
#         self.__index -= 1
#         return value

# 03. Vowels
# class vowels:
#
#     _vowels = ["a", "e", "i", "o", "u", "y"]
#
#     def __init__(self, received_string: str):
#         self.received_string = received_string
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index >= len(self.received_string):
#             raise StopIteration
#         ch = self.received_string[self._index]
#         self._index += 1
#         if ch.lower() not in self._vowels:
#             return self.__next__()
#         return ch

# 04. Squares
# def squares(n):
#     for i in range(1, n+1):
#         yield i ** 2

# 05. Generator Range
# def genrange(start, end):
#     for i in range(start, end + 1):
#         yield i

# 06. Reverse string
# def reverse_text(string):
#
#     for i in reversed(string):
#         yield i
