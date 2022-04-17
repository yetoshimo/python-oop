# 02. Encryption Generator
# class EncryptionGenerator:
#
#     def __init__(self, text: str):
#         self.text = text
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise ValueError("You must add a number.")
#         temp = ""
#         for i in self.text:
#             if ord(i) + other < 32:
#                 temp += chr(ord(i) + other + 95)
#             elif ord(i) + other > 126:
#                 temp += chr(ord(i) + other - 95)
#             else:
#                 temp += chr(ord(i) + other)
#         return temp
#
#
# some_text = EncryptionGenerator('I Love Python!')
# print(some_text + 1)
# print('J!Mpwf!Qzuipo"' == some_text + 1)
# print(some_text + (-1))
# print("H~Knud~Oxsgnm " == some_text + (-1))
#
# example = EncryptionGenerator('Super-Secret Message')
# print(example + 20)
# print("g*%y'Agyw'y)4ay((u{y" == example + 20)
# print(example + (-52))
# print("~A<1>X~1/>1@Kx1??-31" == example + (-52))

# 03. Image Area
# class ImageArea:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.get_area() == other.get_area()
#
#     def __ne__(self, other):
#         return self.get_area() != other.get_area()
#
#     def __gt__(self, other):
#         return self.get_area() > other.get_area()
#
#     def __ge__(self, other):
#         return self.get_area() >= other.get_area()
#
#     def __lt__(self, other):
#         return self.get_area() < other.get_area()
#
#     def __le__(self, other):
#         return self.get_area() <= other.get_area()

# 04. Playing
# def start_playing(instance):
#     return instance.play()

# 05. Shapes
# from abc import ABC, abstractmethod
# from math import pi
#
#
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         return
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         return
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return pi * self.radius * 2
#
#
# class Rectangle(Shape):
#
#     def __init__(self, height, wight):
#         self.height = height
#         self.width = wight
#
#     def calculate_area(self):
#         return self.height * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.height + self.width)
