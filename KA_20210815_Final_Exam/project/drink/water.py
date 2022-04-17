from project.drink.drink import Drink


class Water(Drink):
    default_cost = 1.5

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.default_cost, brand)
