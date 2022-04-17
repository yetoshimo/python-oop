from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age):
        Cat.__init__(self, name, age, gender="Female")

    def make_sound(self):
        return "Meow"
