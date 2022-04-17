from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets: list = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        try:
            find_p = [p for p in self.planets if p.name == name][0]
            return find_p
        except IndexError:
            pass
