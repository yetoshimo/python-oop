from abc import ABC, abstractmethod


class Card(ABC):

    @abstractmethod
    def __init__(self, name: str, damage_points: int, health_points: int):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @staticmethod
    def __check_name(value):
        if value == "" or value is None:
            raise ValueError("Card's name cannot be an empty string.")

    @staticmethod
    def __check_damage_points(value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")

    @staticmethod
    def __check_health_points(value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__check_name(value)
        self._name = value

    @property
    def damage_points(self):
        return self._damage_points

    @damage_points.setter
    def damage_points(self, value):
        self.__check_damage_points(value)
        self._damage_points = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self.__check_health_points(value)
        self._health_points = value
