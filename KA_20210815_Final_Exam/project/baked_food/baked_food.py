from abc import ABC, abstractmethod


class BakedFood(ABC):

    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @staticmethod
    def __validate_name(value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self._name = value

    @staticmethod
    def __validate_price(value):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self._price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
