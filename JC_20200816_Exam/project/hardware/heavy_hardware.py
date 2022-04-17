from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    default_type = "Heavy"
    capacity_modifier = 2
    memory_modifier = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         HeavyHardware.default_type,
                         int(capacity * HeavyHardware.capacity_modifier),
                         int(memory * HeavyHardware.memory_modifier))
