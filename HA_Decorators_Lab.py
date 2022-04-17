# 01. Number Increment
# def number_increment(numbers):
#     def increase():
#         return [x + 1 for x in numbers]
#
#     return increase()


# 02. Vowel Filter
# def vowel_filter(function):
#     def wrapper():
#         _vowels = ["a", "e", "i", "o", "u"]
#         return [i for i in function() if i.lower() in _vowels]
#
#     return wrapper


# 03. Even Numbers
# def even_numbers(function):
#     def wrapper(numbers):
#
#         return [i for i in numbers if i % 2 == 0]
#
#     return wrapper


# 04. Multiply
# from functools import wraps
#
#
# def multiply(times):
#     def decorator(function):
#         wraps(function)
#
#         def wrapper(*args, **kwargs):
#             return function(*args) * times
#
#         return wrapper
#
#     return decorator
