from project.software.software import Software


class ExpressSoftware(Software):
    capacity_consumption_modifier = 1
    memory_consumption_modifier = 2
    default_type = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         self.default_type,
                         int(capacity_consumption * self.capacity_consumption_modifier),
                         int(memory_consumption * self.memory_consumption_modifier))
