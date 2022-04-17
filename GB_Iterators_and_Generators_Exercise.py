# 01. Take Skip
# class take_skip:
#
#     def __init__(self, step: int, count: int):
#         self.count = count
#         self.step = step
#         self._counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self._counter
#         if value > self.step * self.count - 1:
#             raise StopIteration
#         self._counter += self.step
#         return value

# 02. Dictionary Iterator
# class dictionary_iter:
#
#     def __init__(self, dictionary: dict):
#         self.dictionary = dictionary
#         self._keys = list(self.dictionary.keys())
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index >= len(self._keys):
#             raise StopIteration
#         key = self._keys[self._index]
#         value = self.dictionary[key]
#         self._index += 1
#         return key, value

# 03. Countdown Iterator
# class countdown_iterator:
#
#     def __init__(self, count):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < 0:
#             raise StopIteration
#         value = self.count
#         self.count -= 1
#         return value

# 04. Sequence Repeat
# class sequence_repeat:
#
#     def __init__(self, sequence, number):
#         self.number = number
#         self.sequence = sequence
#         self._new_sequence = []
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if len(self._new_sequence) >= self.number:
#             raise StopIteration
#         item = self.sequence[self._index]
#         self._new_sequence.append(item)
#         self._index += 1
#         if self._index >= len(self.sequence):
#             self._index = 0
#         return item

# 05. Take Halves
# def solution():
#     def integers():
#         _integer = 1
#         while True:
#             yield _integer
#             _integer += 1
#
#     def halves():
#         for i in integers():
#             yield i / 2
#
#     def take(n, seq):
#         _result = []
#         for i in seq:
#             if len(_result) == n:
#                 return _result
#             _result.append(i)
#
#     return (take, halves, integers)

# 06. Fibonacci Generator
# def fibonacci():
#
#     a = 0
#     b = 1
#
#     while True:
#         yield a
#         a, b = b, a + b

# 07. Reader
# def read_next(*args):
#     for item in args:
#         for element in item:
#             yield element

# # 08. Prime Numbers
# def get_primes(numbers: list):
#
#     for item in numbers:
#
#         if item < 2:
#             continue
#
#         _is_prime = True
#
#         for i in range(2, item):
#
#             if (item % i) == 0:
#                 _is_prime = False
#                 break
#
#         if _is_prime:
#             yield item

# 09. Possible permutations
# from itertools import permutations
#
#
# def possible_permutations(input_list: list):
#
#     perm = permutations(input_list)
#
#     for _ in perm:
#
#         yield list(_)
