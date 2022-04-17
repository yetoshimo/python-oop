from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    default_type = "Power"
    capacity_modifier = 0.25
    memory_modifier = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         PowerHardware.default_type,
                         int(capacity * PowerHardware.capacity_modifier),
                         int(memory * PowerHardware.memory_modifier))
