from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity
