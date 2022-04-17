from project.software.software import Software


class Hardware:

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.memory = memory
        self.capacity = capacity
        self.type = type
        self.name = name
        self.software_components: list = []

    @property
    def used_capacity(self):
        _used_capacity = sum([item.capacity_consumption for item in self.software_components])
        return _used_capacity

    @property
    def used_memory(self):
        _used_memory = sum([item.memory_consumption for item in self.software_components])
        return _used_memory

    def __install_check(self, software):
        if (self.used_memory + software.memory_consumption) > self.memory:
            raise Exception("Software cannot be installed")
        elif (self.used_capacity + software.capacity_consumption) > self.capacity:
            raise Exception("Software cannot be installed")

    def install(self, software: Software):
        self.__install_check(software)
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)
