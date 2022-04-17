from abc import ABC

from project.survivor import Survivor


class Medicine(ABC):

    def __init__(self, health_increase: int):
        self.health_increase = health_increase

    @staticmethod
    def __validate_health_increase(value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")

    @property
    def health_increase(self):
        return self._health_increase

    @health_increase.setter
    def health_increase(self, value):
        self.__validate_health_increase(value)
        self._health_increase = value

    def apply(self, survivor: Survivor):
        survivor.health += self.health_increase
