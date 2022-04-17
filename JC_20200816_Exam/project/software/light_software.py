from project.software.software import Software


class LightSoftware(Software):
    default_type = "Light"
    capacity_consumption_modifier = 1.5
    memory_consumption_modifier = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         LightSoftware.default_type,
                         int(capacity_consumption * LightSoftware.capacity_consumption_modifier),
                         int(memory_consumption * LightSoftware.memory_consumption_modifier))
