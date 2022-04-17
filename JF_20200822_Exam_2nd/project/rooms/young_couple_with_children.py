from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    appliances = []
    default_members = 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.default_members += len(children)
        self.appliances = self.__generate_appliances(self.default_members)
        super().__init__(family_name, salary_one + salary_two, self.default_members)
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)

    @staticmethod
    def __generate_appliances(member_count):
        _appliances = []

        for i in range(member_count):
            _appliances.append(TV())
            _appliances.append(Fridge())
            _appliances.append(Laptop())

        return _appliances
