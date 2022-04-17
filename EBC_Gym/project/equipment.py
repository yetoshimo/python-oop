class Equipment:
    equipment_id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id + 1
