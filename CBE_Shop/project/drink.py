from project.product import Product


class Drink(Product):
    drink_quantity = 10

    def __init__(self, name: str):
        super(Drink, self).__init__(name, Drink.drink_quantity)
