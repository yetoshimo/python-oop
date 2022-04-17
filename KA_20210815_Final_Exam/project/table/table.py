from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.capacity = capacity
        self.table_number = table_number
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @staticmethod
    def __validate_capacity(value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self._capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"

    @property
    def ordered_food(self):
        return [
            f"Table {self.table_number} ordered:",
            *[str(f) for f in self.food_orders]
        ]

    @property
    def ordered_drinks(self):
        return [
            f"Table {self.table_number} ordered:",
            *[str(d) for d in self.drink_orders]
        ]
