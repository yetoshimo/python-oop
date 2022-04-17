from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    _successful = 0
    _unsuccessful = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == "Biologist":
            a = Biologist(name)

        elif astronaut_type == "Geodesist":
            a = Geodesist(name)

        elif astronaut_type == "Meteorologist":
            a = Meteorologist(name)

        else:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{a.name} is already added."
        self.astronaut_repository.add(a)
        return f"Successfully added {a.__class__.__name__}: {a.name}."

    def add_planet(self, name: str, items: str):
        p = Planet(name)
        p.items = items.split(", ")
        if self.planet_repository.find_by_name(name):
            return f"{p.name} is already added."
        self.planet_repository.add(p)
        return f"Successfully added Planet: {p.name}."

    def retire_astronaut(self, name: str):
        if self.astronaut_repository.find_by_name(name):
            a = self.astronaut_repository.find_by_name(name)
            self.astronaut_repository.remove(a)
            return f"Astronaut {a.name} was retired!"
        else:
            raise Exception(f"Astronaut {name} doesn't exists!")

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        p = self.planet_repository.find_by_name(planet_name)
        if p:
            _selected_astronauts = sorted(self.astronaut_repository.suitable_astronauts(), key=lambda kv: -kv.oxygen)
            if not _selected_astronauts:
                raise Exception("You need at least one astronaut to explore the planet!")
            if len(_selected_astronauts) > 5:
                _selected_astronauts = _selected_astronauts[:5]
            _eva_astronauts = []
            for a in _selected_astronauts:
                while p.items:
                    if a not in _eva_astronauts:
                        _eva_astronauts.append(a)
                    a.add_item(p.items.pop())
                    a.breathe()
                    if a.oxygen <= 0:
                        break

            if not p.items:
                self._successful += 1
                return f"Planet: {p.name} was explored. {len(_eva_astronauts)} " \
                       f"astronauts participated in collecting items."
            else:
                self._unsuccessful += 1
                return f"Mission is not completed."

        else:
            raise Exception("Invalid planet name!")

    def report(self):
        result = [f"{self._successful} successful missions!",
                  f"{self._unsuccessful} missions were not completed!",
                  f"Astronauts' info:",
                  *[str(a) for a in self.astronaut_repository.astronauts]
                  ]
        return '\n'.join(result)


# ss = SpaceStation()
# # print(ss.add_astronaut("Biologist", "test_b1"))
# # print(ss.add_astronaut("Biologist", "test_b2"))
# # print(ss.add_astronaut("Biologist", "test_b3"))
# # print(ss.add_astronaut("Biologist", "test_b"))
# # print(ss.add_astronaut("Geodesist", "test_g1"))
# # print(ss.add_astronaut("Geodesist", "test_g2"))
# # print(ss.add_astronaut("Geodesist", "test_g"))
# # print(ss.add_astronaut("Meteorologist", "test_m1"))
# # print(ss.add_astronaut("Meteorologist", "test_m2"))
# # print(ss.add_astronaut("Meteorologist", "test_m3"))
# # print(ss.add_astronaut("Meteorologist", "test_m"))
# # print(ss.astronaut_repository.astronauts)
# # print(ss.add_astronaut("mahmut", "test_tuncer"))
# # print(ss.add_planet("test_planet", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"))
# ss.add_planet("test_planet", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
# # print(ss.add_planet("test_planet", "mahmut, tuncer"))
# # print(ss.retire_astronaut("test_b"))
# # print(ss.astronaut_repository.astronauts)
# # print(ss.retire_astronaut("test_b"))
# # [print(o.oxygen) for o in ss.astronaut_repository.astronauts]
# # ss.recharge_oxygen()
# # [print(o.oxygen) for o in ss.astronaut_repository.astronauts]
# ss.add_astronaut("Biologist", "test_b1")
# ss.add_astronaut("Biologist", "test_b2")
# ss.add_astronaut("Biologist", "test_b3")
# ss.add_astronaut("Geodesist", "test_g1")
# ss.add_astronaut("Geodesist", "test_g2")
# ss.add_astronaut("Meteorologist", "test_m1")
# ss.add_astronaut("Meteorologist", "test_m2")
# ss.add_astronaut("Meteorologist", "test_m3")
# # [print(a) for a in ss.astronaut_repository.astronauts]
# ss.send_on_mission("test_planet")
# print(ss.report())
