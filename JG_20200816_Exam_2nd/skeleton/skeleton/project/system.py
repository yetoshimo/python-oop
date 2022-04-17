from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware: list = []
    _software: list = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            h = [h for h in System._hardware if h.name == hardware_name][0]
            es = ExpressSoftware(name, capacity_consumption, memory_consumption)
            h.install(es)
            System._software.append(es)
        except IndexError:
            return "Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            h = [h for h in System._hardware if h.name == hardware_name][0]
            ls = LightSoftware(name, capacity_consumption, memory_consumption)
            h.install(ls)
            System._software.append(ls)
        except IndexError:
            return "Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            h = [h for h in System._hardware if h.name == hardware_name][0]
            s = [s for s in System._software if s.name == software_name][0]
            h.uninstall(s)
            System._software.remove(s)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ""
        result += "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {sum(h.used_memory for h in System._hardware)} /" \
                  f" {sum(h.memory for h in System._hardware)}\n"
        result += f"Total Capacity Taken: {sum(h.used_capacity for h in System._hardware)} /" \
                  f" {sum(h.capacity for h in System._hardware)}"
        return result

    @staticmethod
    def system_split():
        result = [str(h) for h in System._hardware]
        return ''.join(result)
