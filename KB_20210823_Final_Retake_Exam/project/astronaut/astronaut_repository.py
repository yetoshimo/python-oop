from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts: list = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        try:
            find_a = [a for a in self.astronauts if a.name == name][0]
            return find_a
        except IndexError:
            pass

    def suitable_astronauts(self):
        return [a for a in self.astronauts if a.oxygen > 30]
