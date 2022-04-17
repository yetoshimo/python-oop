from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Fruit) or isinstance(food, Vegetable):
            self.weight += food.quantity * 0.1
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.4
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += food.quantity * 0.3
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
