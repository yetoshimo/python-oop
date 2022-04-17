from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    default_breathe = 15
    default_oxygen = 90

    def __init__(self, name: str):
        super().__init__(name, self.default_oxygen)
