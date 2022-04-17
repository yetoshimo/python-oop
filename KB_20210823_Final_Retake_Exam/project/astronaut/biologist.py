from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    default_breathe = 5
    default_oxygen = 70

    def __init__(self, name: str):
        super().__init__(name, self.default_oxygen)
