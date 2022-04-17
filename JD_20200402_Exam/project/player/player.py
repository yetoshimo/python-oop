from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):

    @abstractmethod
    def __init__(self, username: str, health: int):
        self.health = health
        self.username = username
        self.card_repository = CardRepository()

    @staticmethod
    def __check_username(value):
        if value == "" or value is None:
            raise ValueError("Player's username cannot be an empty string.")

    @staticmethod
    def __check_health(value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")

    @staticmethod
    def __check_damage_points(value):
        if value < 0:
            raise ValueError("Damage points cannot be less than zero.")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self.__check_username(value)
        self._username = value

    @property
    def health(self):
        return self._health

    @property
    def is_dead(self):
        return self.health <= 0

    @health.setter
    def health(self, value):
        self.__check_health(value)
        self._health = value

    def take_damage(self, damage_points: int):
        self.__check_damage_points(damage_points)
        self.health -= damage_points
