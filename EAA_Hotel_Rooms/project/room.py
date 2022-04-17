class Room:
    def __init__(self, number: int, capacity: int):
        self.capacity = capacity
        self.number = number
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_take_room(_is_taken, _people, _capacity):
        return not _is_taken and _people <= _capacity

    @staticmethod
    def can_free_room(_is_taken):
        return _is_taken

    def take_room(self, people):
        if not self.can_take_room(self.is_taken, people, self.capacity):
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.can_free_room(self.is_taken):
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0
