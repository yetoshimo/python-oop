# 01. Vet
# class Vet:
#     animals = []  # it will store the total amount of animals for all vets
#     space = 5
#
#     def __init__(self, name: str):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if not Vet.space:
#             return f"Not enough space"
#         Vet.animals.append(animal_name)
#         Vet.space -= 1
#         self.animals.append(animal_name)
#         return f"{animal_name} registered in the clinic"
#
#     def unregister_animal(self, animal_name):
#         if animal_name not in Vet.animals:
#             return f"{animal_name} not in the clinic"
#         Vet.animals.remove(animal_name)
#         Vet.space += 1
#         self.animals.remove(animal_name)
#         return f"{animal_name} unregistered successfully"
#
#     def info(self):
#         return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())

# 02. Time
# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours: int, minutes: int, seconds: int):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
#
#     def next_second(self):
#         if self.seconds + 1 <= Time.max_seconds:
#             self.seconds += 1
#             return Time.get_time(self)
#         else:
#             self.seconds = self.seconds - Time.max_seconds
#             if self.minutes + 1 <= Time.max_minutes:
#                 self.minutes += 1
#                 return Time.get_time(self)
#             else:
#                 self.minutes = self.minutes - Time.max_minutes
#                 if self.hours + 1 <= Time.max_hours:
#                     self.hours += 1
#                     return Time.get_time(self)
#                 else:
#                     self.hours = self.hours - Time.max_hours
#                     return Time.get_time(self)
#
#
# time = Time(9, 30, 59)
# print(time.next_second())
#
# time = Time(10, 59, 59)
# print(time.next_second())
#
# time = Time(23, 59, 59)
# print(time.next_second())
#
# time = Time(16, 35, 54)
# print(time.next_second())
#
# time = Time(1, 20, 30)
# print(time.next_second())
#
# time = Time(1, 59, 59)
# print(time.next_second())
#
# time = Time(0, 0, 0)
# print(time.next_second())

# 03. Account
# class Account:
#     def __init__(self, id: int, name: str, balance: int = 0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if self.balance - amount < 0:
#             return f"Amount exceeded balance"
#         self.balance -= amount
#         return self.balance
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
#
#
# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())
#
# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())

# 04. Pizza Delivery
# class PizzaDelivery:
#
#     def __init__(self, name: str, price: float, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             self.ingredients[ingredient] = quantity
#             self.price += quantity * ingredient_price
#             return
#         self.ingredients[ingredient] += quantity
#         self.price += quantity * ingredient_price
#         return
#
#     def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         if quantity > self.ingredients[ingredient]:
#             return f"Please check again the desired quantity of {ingredient}!"
#         self.ingredients[ingredient] -= quantity
#         self.price -= quantity * ingredient_price
#         return
#
#     def make_order(self):
#         self.ordered = True
#         return f"You've ordered pizza {self.name} prepared with {', '.join([key+': '+str(value) for key, value in self.ingredients.items()])} and the price will be {self.price}lv."
#
#
# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
