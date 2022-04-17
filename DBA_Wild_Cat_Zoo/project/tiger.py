from project.animal import Animal


class Tiger(Animal):

    def __init__(self, name: str, gender: str, age: int):
        super(Tiger, self).__init__(name, gender, age)

    @staticmethod
    def get_needs():
        return 45
