# 01. Logged
# def logged(function):
#     def wrapper(*args):
#         return f"you called {function.__name__}{args}\nit returned {function(*args)}"
#
#     return wrapper

# 02. Even Parameters
# def even_parameters(function):
#     def wrapper(*args):
#         for i in args:
#             if not type(i) == int:
#                 return f"Please use only even numbers!"
#             if i % 2 != 0:
#                 return f"Please use only even numbers!"
#         return function(*args)
#
#     return wrapper

# 03. Bold, Italic, Underline
# def make_bold(func):
#     def wrapper(*args):
#         return f"<b>{func(*args)}</b>"
#
#     return wrapper
#
#
# def make_italic(func):
#     def wrapper(*args):
#         return f"<i>{func(*args)}</i>"
#
#     return wrapper
#
#
# def make_underline(func):
#     def wrapper(*args):
#         return f"<u>{func(*args)}</u>"
#
#     return wrapper

# 04. Type Check
# def type_check(_type):
#     def decorator(func):
#         def wrapper(*args):
#             if type(*args) == _type:
#                 return func(*args)
#             return f"Bad Type"
#
#         return wrapper
#
#     return decorator

# 05. Cache
# from functools import wraps
#
#
# def cache(func):
#     wraps(func)
#
#     def wrapper(*args, **kwargs):
#         cache_key = args[0]
#         if cache_key not in wrapper.log:
#             wrapper.log[cache_key] = func(*args, **kwargs)
#         return wrapper.log[cache_key]
#
#     wrapper.log = {}
#     return wrapper

# 06. HTML Tags
# from functools import wraps
#
#
# def tags(_html):
#     def decorator(func):
#         wraps(func)
#
#         def wrapper(*args):
#             return f"<{_html}>{func(*args)}</{_html}>"
#
#         return wrapper
#
#     return decorator

# 07. Execution Time
# import time
#
#
# def exec_time(func):
#
#     def wrapper(*args):
#         start_time = time.time()
#         func(*args)
#         end_time = time.time()
#         return end_time - start_time
#
#     return wrapper

# 08. Store Results
# class store_results:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         with open("results.txt", mode="a") as file:
#             file.write(f"Function '{self.func.__name__}' was called. Result: {self.func(*args, **kwargs)}\n")
#         return self.func(*args, **kwargs)
