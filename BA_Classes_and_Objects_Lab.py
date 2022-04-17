# 01. Vehicle
# class Vehicle:
#
#     def __init__(self, mileage, max_speed=150):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.gadgets = []
#
#
# car = Vehicle(20)
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)

# 02. Point
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f"The point has coordinates ({self.x},{self.y})"
#
#
# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)

# 03. Circle
# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius: int):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
#     def get_area(self):
#         return self.radius ** 2 * Circle.pi
#
#     def get_circumference(self):
#         return self.radius * 2 * Circle.pi
#
#
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())

# 04. Glass
# class Glass:
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if not Glass.capacity - ml >= 0:
#             return f"Cannot add {ml} ml"
#         self.content += ml
#         Glass.capacity -= ml
#         return f"Glass filled with {ml} ml"
#
#     def empty(self):
#         Glass.capacity += self.content
#         self.content = 0
#         return f"Glass is now empty"
#
#     @staticmethod
#     def info():
#         return f"{Glass.capacity} ml left"
#
#
# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())

# 05. Smartphone
# class Smartphone:
#     def __init__(self, memory: int):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         self.is_on = not self.is_on
#
#     def install(self, app, memory):
#         if self.memory - memory >= 0 and self.is_on:
#             self.apps.append(app)
#             self.memory -= memory
#             return f"Installing {app}"
#         elif self.memory - memory >= 0 and not self.is_on:
#             return f"Turn on your phone to install {app}"
#         else:
#             return f"Not enough memory to install {app}"
#
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
#
#
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())
