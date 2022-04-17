from project.software.software import Software


class Hardware:

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.memory = memory
        self.capacity = capacity
        self.type = type
        self.name = name
        self.software_components: list = []

    @property
    def used_memory(self):
        return sum(s.memory_consumption for s in self.software_components)

    @property
    def used_capacity(self):
        return sum(s.capacity_consumption for s in self.software_components)

    def __check_available_memory(self, software: Software):
        if self.used_memory + software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

    def __check_available_capacity(self, software: Software):
        if self.used_capacity + software.capacity_consumption > self.capacity:
            raise Exception("Software cannot be installed")

    def install(self, software: Software):
        self.__check_available_memory(software)
        self.__check_available_capacity(software)
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __repr__(self):
        result = ""
        result += f"Hardware Component - {self.name}\n"
        result += f"Express Software Components: " \
                  f"{len([c for c in self.software_components if c.__class__.__name__ == 'ExpressSoftware'])}\n"
        result += f"Light Software Components: " \
                  f"{len([c for c in self.software_components if c.__class__.__name__ == 'LightSoftware'])}\n"
        result += f"Memory Usage: {self.used_memory} / {self.memory}\n"
        result += f"Capacity Usage: {self.used_capacity} / {self.capacity}\n"
        result += f"Type: {self.type}\n"
        result += f"Software Components: " \
                  f"{', '.join([s.name for s in self.software_components] if self.software_components else None)}"
        return result
