from abc import ABC, abstractmethod


class Drink(ABC):

    @abstractmethod
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

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
    def __validate_portion(value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

    @property
    def portion(self):
        return self._portion

    @portion.setter
    def portion(self, value):
        self.__validate_portion(value)
        self._portion = value

    @staticmethod
    def __validate_brand(value):
        if value == "" or value.isspace():
            raise ValueError("Brand cannot be empty string or white space!")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self.__validate_brand(value)
        self._brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
