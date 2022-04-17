from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for i in self.products:
            if i.name == product_name:
                return i

    def remove(self, product_name: str):
        for i in self.products:
            if i.name == product_name:
                self.products.remove(i)

    def __repr__(self):
        return '\n'.join([f"{i.name}: {i.quantity}" for i in self.products])
