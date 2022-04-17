from abc import ABC, abstractmethod


class Astronaut(ABC):
    default_breathe = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.oxygen = oxygen
        self.name = name
        self.backpack: list = []

    @staticmethod
    def __validate_name(value):
        if value == "" or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self._name = value

    def breathe(self):
        self.oxygen -= self.default_breathe

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def add_item(self, item):
        self.backpack.append(item)

    def can_breathe(self):
        return self.oxygen - self.default_breathe >= 0

    def __repr__(self):
        # result = f"Astronauts' info:\n"
        result = f"Name: {self.name}\n"
        result += f"Oxygen: {self.oxygen}\n"
        result += f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}"
        return result
