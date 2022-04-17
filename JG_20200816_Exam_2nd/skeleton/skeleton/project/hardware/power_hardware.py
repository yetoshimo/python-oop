from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    capacity_modifier = 0.25
    memory_modifier = 1.75
    default_type = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         self.default_type,
                         int(capacity * self.capacity_modifier),
                         int(memory * self.memory_modifier))
