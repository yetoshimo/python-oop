from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    capacity_modifier = 2
    memory_modifier = 0.75
    default_type = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         self.default_type,
                         int(capacity * self.capacity_modifier),
                         int(memory * self.memory_modifier))
