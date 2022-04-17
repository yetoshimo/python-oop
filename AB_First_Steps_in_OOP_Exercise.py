# 01. Shop
# class Shop:
#     def __init__(self, name, items: list):
#         self.name = name
#         self.items = items
#
#     def get_items_count(self):
#         return len(self.items)
#
#
# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())

# 02. Hero
# class Hero:
#     def __init__(self, name: str, health: int):
#         self.name = name
#         self.health = health
#
#     def defend(self, damage: int):
#         self.health -= damage
#         if self.health <= 0:
#             self.health = 0
#             return f"{self.name} was defeated"
#
#     def heal(self, amount: int):
#         self.health += amount
#
#
# hero = Hero("Peter", 100)
# print(hero.defend(50))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))

# 03. Employee
# class Employee:
#
#     def __init__(self, id: int, first_name: str, last_name: str, salary: int):
#         self.salary = salary
#         self.last_name = last_name
#         self.first_name = first_name
#         self.id = id
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_annual_salary(self):
#         return self.salary * 12
#
#     def raise_salary(self, amount: int):
#         self.salary += amount
#         return self.salary
#
#
# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())

# 04. Cup
# class Cup:
#     def __init__(self, size: int, quantity: int):
#         self.size = size
#         self.quantity = quantity
#
#     def fill(self, _milliliters):
#         if self.quantity + _milliliters <= self.size:
#             self.quantity += _milliliters
#         return
#
#     def status(self):
#         return self.size - self.quantity
#
#
# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())

# 05. Flower
# class Flower:
#     def __init__(self, name: str, water_requirements: int):
#         self.name = name
#         self.water_requirements = water_requirements
#         self.is_happy = False
#
#     def water(self, _quantity):
#         self.is_happy = _quantity >= self.water_requirements
#
#     def status(self):
#         if self.is_happy:
#             return f"{self.name} is happy"
#         else:
#             return f"{self.name} is not happy"
#
#
# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(60)
# print(flower.status())
# flower.water(100)
# print(flower.status())

# 06. Steam User
# class SteamUser:
#     def __init__(self, username: str, games: list):
#         self.username = username
#         self.games = games
#         self.played_hours = 0
#
#     def play(self, game: str, hours: int):
#         if game in self.games:
#             self.played_hours += hours
#             return f"{self.username} is playing {game}"
#         else:
#             return f"{game} is not in library"
#
#     def buy_game(self, game: str):
#         if game not in self.games:
#             self.games.append(game)
#             return f"{self.username} bought {game}"
#         else:
#             return f"{game} is already in your library"
#
#     def status(self):
#         return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
#
#
# user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
# print(user.play("Fortnite", 3))
# print(user.play("Oxygen Not Included", 5))
# print(user.buy_game("CS:GO"))
# print(user.buy_game("Oxygen Not Included"))
# print(user.play("Oxygen Not Included", 6))
# print(user.status())

# 07. Programmer
# class Programmer:
#     def __init__(self, name: str, language: str, skills: int):
#         self.name = name
#         self.language = language
#         self.skills = skills
#
#     def watch_course(self, course_name: str, language: str, skills_earned: int):
#         if self.language == language:
#             self.skills += skills_earned
#             return f"{self.name} watched {course_name}"
#         # else:
#         return f"{self.name} does not know {language}"
#
#     def change_language(self, new_language: str, skills_needed: int):
#         if new_language != self.language:
#             if self.skills >= skills_needed:
#                 _temp_language = self.language
#                 self.language = new_language
#                 return f"{self.name} switched from {_temp_language} to {self.language}"
#             # else:
#             return f"{self.name} needs {skills_needed - self.skills} more skills"
#         # else:
#         return f"{self.name} already knows {self.language}"
#
#
# programmer = Programmer("John", "Java", 50)
# print(programmer.watch_course("Python Masterclass", "Python", 84))
# print(programmer.change_language("Java", 30))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Java: zero to hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python Masterclass", "Python", 84))
