from project.software.software import Software


class ExpressSoftware(Software):
    default_type = "Express"
    capacity_consumption_modifier = 1
    memory_consumption_modifier = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         ExpressSoftware.default_type,
                         int(capacity_consumption * ExpressSoftware.capacity_consumption_modifier),
                         int(memory_consumption * ExpressSoftware.memory_consumption_modifier))
