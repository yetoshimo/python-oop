from project.mammal import Mammal


class Bear(Mammal):

    def __init__(self, name: str):
        super(Bear, self).__init__(name)
