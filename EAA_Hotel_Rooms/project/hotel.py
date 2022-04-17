class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room(_rooms, _room_number):
        return next(filter(lambda room: room.number == _room_number, _rooms))

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        _result = self.find_room(self.rooms, room_number).take_room(people)
        if not _result:
            self.guests += people
            return _result

    def free_room(self, room_number):
        _room = self.find_room(self.rooms, room_number)
        _guests = _room.guests
        _result = _room.free_room()
        if not _result:
            self.guests -= _guests
            return _result

    def status(self):
        _free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        _occupied_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        response = f"Hotel {self.name} has {self.guests} total guests\n"
        response += f"Free rooms: {', '.join(_free_rooms)}\n"
        response += f"Taken rooms: {', '.join(_occupied_rooms)}"
        return response
