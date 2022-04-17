# 01. Vehicles
# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_consumption = fuel_consumption
#         self.fuel_quantity = fuel_quantity
#
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#     @abstractmethod
#     def refuel(self, fuel):
#         pass
#
#
# class Car(Vehicle):
#
#     CONSUMPTION_INCREASE = 0.9
#
#     def drive(self, distance):
#         fuel_needed = distance * (self.fuel_consumption + Car.CONSUMPTION_INCREASE)
#         if fuel_needed > self.fuel_quantity:
#             return
#         self.fuel_quantity -= fuel_needed
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#         return self.fuel_quantity
#
#
# class Truck(Vehicle):
#
#     CONSUMPTION_INCREASE = 1.6
#
#     def drive(self, distance):
#         fuel_needed = distance * (self.fuel_consumption + Truck.CONSUMPTION_INCREASE)
#         if fuel_needed > self.fuel_quantity:
#             return
#         self.fuel_quantity -= fuel_needed
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel * 0.95
#         return self.fuel_quantity

# 02. Groups
# class Person:
#
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname
#
#     def __add__(self, other):
#         return Person(self.name, other.surname)
#
#     def __repr__(self):
#         return self.name + ' ' + self.surname
#
#
# class Group:
#
#     def __init__(self, name: str, people: [Person]):
#         self.name = name
#         self.people = people
#
#     def __len__(self):
#         return len(self.people)
#
#     def __repr__(self):
#         return f"Group {self.name} with members {', '.join([i.name + ' ' + i.surname for i in self.people])}"
#
#     def __add__(self, other):
#         return Group(self.name + " " + other.name, self.people + other.people)
#
#     def __getitem__(self, item):
#         return f"Person {item}: {self.people[item].name} {self.people[item].surname}"

# 03. Account
# class Account:
#
#     def __init__(self, owner: str, amount=0):
#         self.owner = owner
#         self.amount = amount
#         self._transactions = []
#
#     @property
#     def balance(self):
#         return self.amount + sum(self._transactions)
#
#     @staticmethod
#     def validate_transaction(account, amount_to_add):
#         if account.balance + amount_to_add < 0:
#             raise ValueError('sorry cannot go in debt!')
#         account.add_transaction(amount_to_add)
#         return f"New balance: {account.balance}"
#
#     def add_transaction(self, amount):
#         if not isinstance(amount, int):
#             raise ValueError('please use int for amount')
#         self._transactions.append(amount)
#
#     def __str__(self):
#         return f"Account of {self.owner} with starting amount: {self.amount}"
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.owner}, {self.amount})"
#
#     def __len__(self):
#         return len(self._transactions)
#
#     def __iter__(self):
#         return iter(self._transactions)
#
#     def __getitem__(self, item):
#         return self._transactions[item]
#
#     def __gt__(self, other):
#         return self.balance > other.balance
#
#     def __ge__(self, other):
#         return self.balance >= other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     def __le__(self, other):
#         return self.balance <= other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __ne__(self, other):
#         return self.balance != other.balance
#
#     def __add__(self, other):
#         _new_account = Account(self.owner + '&' + other.owner, self.amount + other.amount)
#         _new_account._transactions = self._transactions + other._transactions
#         return _new_account
