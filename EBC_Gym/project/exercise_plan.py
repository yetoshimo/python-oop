class ExercisePlan:
    exercise_id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.duration = duration
        self.equipment_id = equipment_id
        self.trainer_id = trainer_id
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @staticmethod
    def get_next_id():
        return ExercisePlan.exercise_id + 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)
