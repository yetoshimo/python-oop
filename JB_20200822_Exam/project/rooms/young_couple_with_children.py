from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    default_member_count = 2
    room_cost = 30
    appliances = []

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.default_member_count += len(children)
        super().__init__(family_name, salary_one + salary_two, self.default_member_count)
        self.__generate_appliances(self.appliances)
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)

    def __generate_appliances(self, default_appliances):
        for i in range(self.default_member_count):
            default_appliances.append(TV())
            default_appliances.append(Fridge())
            default_appliances.append(Laptop())
