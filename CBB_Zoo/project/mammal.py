from project.animal import Animal


class Mammal(Animal):

    def __init__(self, name: str):
        super(Mammal, self).__init__(name)
