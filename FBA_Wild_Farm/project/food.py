from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):

    def __init__(self, quantity: int):
        Food.__init__(self, quantity)


class Fruit(Food):

    def __init__(self, quantity: int):
        Food.__init__(self, quantity)


class Meat(Food):

    def __init__(self, quantity: int):
        Food.__init__(self, quantity)


class Seed(Food):

    def __init__(self, quantity: int):
        Food.__init__(self, quantity)
