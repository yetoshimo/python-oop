# 01. Calculator
# class Calculator:
#     @staticmethod
#     def add(*args):
#         return sum(args)
#
#     @staticmethod
#     def multiply(*args):
#         _result = 1
#         for _ in args:
#             _result *= _
#         return _result
#
#     @staticmethod
#     def divide(first_number, *args):
#         _result = first_number
#         for _ in args:
#             _result /= _
#         return _result
#
#     @staticmethod
#     def subtract(first_number, *args):
#         _result = first_number
#         for _ in args:
#             _result -= _
#         return _result
#
#
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))

# 02. Shop
# class Shop:
#     def __init__(self, name: str, type: str, capacity: int):
#         self.capacity = capacity
#         self.type = type
#         self.name = name
#         self.items = {}  # stores name of an item and its quantity item_name: quantity
#
#     def __repr__(self):
#         return f"{self.name} of type {self.type} with capacity {self.capacity}"
#
#     @staticmethod
#     def small_shop(name: str, type: str):
#         return Shop(name, type, 10)
#
#     def add_item(self, item_name: str):
#         if not sum(self.items.values()) < self.capacity:
#             return f"Not enough capacity in the shop"
#         if item_name not in self.items:
#             self.items[item_name] = 0
#         self.items[item_name] += 1
#         return f"{item_name} added to the shop"
#
#     def remove_item(self, item_name: str, amount: int):
#         if item_name not in self.items or self.items[item_name] < amount:
#             return f"Cannot remove {amount} {item_name}"
#         self.items[item_name] -= amount
#         return f"{amount} {item_name} removed from the shop"
#
#
# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))

# 03. Integer
# class Integer:
#
#     def __init__(self, value: int):
#         self.value = value
#
#     @staticmethod
#     def is_float(_value):
#         return isinstance(_value, float)
#
#     @staticmethod
#     def int_from_str(_value):
#         return isinstance(_value, float)
#
#     @staticmethod
#     def roman_to_integer(_value):
#         roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
#                          'XC': 90, 'CD': 400, 'CM': 900}
#         i = 0
#         num = 0
#         while i < len(_value):
#             if i + 1 < len(_value) and _value[i:i + 2] in roman_numbers:
#                 num += roman_numbers[_value[i:i + 2]]
#                 i += 2
#             else:
#                 num += roman_numbers[_value[i]]
#                 i += 1
#         return num
#
#     @staticmethod
#     def is_integer_instance(_integer):
#         return type(_integer) == Integer
#
#     @classmethod
#     def from_float(cls, value):
#         if not cls.is_float(value):
#             return f"value is not a float"
#         return cls(int(value))
#
#     @classmethod
#     def from_string(cls, value):
#         if cls.int_from_str(value):
#             return f"wrong type"
#         return cls(int(value))
#
#     @classmethod
#     def from_roman(cls, value):
#         return cls(cls.roman_to_integer(value))
#
#     # def add(self, integer):
#     #     if not self.is_integer_instance(integer):
#     #         return f"number should be an Integer instance"
#     #     return self.value + integer.value
#
#
# first_num = Integer(10)
# second_num = Integer.from_roman("IV")
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
