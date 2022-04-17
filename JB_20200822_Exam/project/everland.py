from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.total_room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        payment_results = [self.__pay_for_room(room) for room in self.rooms]
        return '\n'.join(payment_results)

    def __pay_for_room(self, room: Room):
        if room.budget >= room.total_room_cost:
            room.budget -= room.total_room_cost
            return f"{room.family_name} paid {room.total_room_cost:.2f}$ and have {room.budget:.2f}$ left."
        else:
            self.__remove_room(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."

    def __remove_room(self, room: Room):
        self.rooms.remove(room)

    def status(self):
        everland_status = [str(r) for r in self.rooms]
        result = [
            f"Total population: {sum(r.members_count for r in self.rooms)}",
            *everland_status
        ]
        return '\n'.join(result)
