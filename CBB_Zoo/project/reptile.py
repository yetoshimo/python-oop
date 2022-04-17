from project.animal import Animal


class Reptile(Animal):

    def __init__(self, name: str):
        super(Reptile, self).__init__(name)
