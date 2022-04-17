from project.person import Person


class Child(Person):

    def __init__(self, name: str, age: int):
        super(Child, self).__init__(name, age)
