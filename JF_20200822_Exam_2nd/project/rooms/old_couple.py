from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
    default_members = 2

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self.default_members)
        self.calculate_expenses(self.appliances)
