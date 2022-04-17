from project.product import Product


class Food(Product):
    food_quantity = 15

    def __init__(self, name: str):
        super(Food, self).__init__(name, Food.food_quantity)
