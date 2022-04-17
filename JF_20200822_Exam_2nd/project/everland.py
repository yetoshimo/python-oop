from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        _total_consumption = sum(room.total_room_cost for room in self.rooms)
        return f"Monthly consumption: {_total_consumption:.2f}$."

    def pay(self):
        _result = []
        for room in self.rooms:
            if room.budget >= room.total_room_cost:
                room.budget -= room.total_room_cost
                _result.append(f"{room.family_name} paid {room.total_room_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                _result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(_result)

    def status(self):
        _rooms_results = [str(room) for room in self.rooms]
        _result = [
            f"Total population: {sum(room.members_count for room in self.rooms)}",
            *_rooms_results
        ]
        return '\n'.join(_result)
