from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware: list = []
    _software: list = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware_to_use = [h for h in System._hardware if h.name == hardware_name][0]
            software_to_install = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware_to_use.install(software_to_install)
            System._software.append(software_to_install)
        except IndexError:
            return "Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware_to_use = [h for h in System._hardware if h.name == hardware_name][0]
            software_to_install = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware_to_use.install(software_to_install)
            System._software.append(software_to_install)
        except IndexError:
            return "Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware_to_use = [h for h in System._hardware if h.name == hardware_name][0]
            software_to_uninstall = [s for s in System._software if s.name == software_name][0]
            hardware_to_use.uninstall(software_to_uninstall)
            System._software.remove(software_to_uninstall)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ""
        result += "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {sum([h.used_memory for h in System._hardware])} " \
                  f"/ {sum([h.memory for h in System._hardware])}\n"
        result += f"Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} " \
                  f"/ {sum([h.capacity for h in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for item in System._hardware:
            result += f"Hardware Component - {item.name}\n"
            result += f"Express Software Components: " \
                      f"{len([es for es in item.software_components if es.type == 'Express'])}\n"
            result += f"Light Software Components: " \
                      f"{len([ls for ls in item.software_components if ls.type == 'Light'])}\n"
            result += f"Memory Usage: {item.used_memory} / {item.memory}\n"
            result += f"Capacity Usage: {item.used_capacity} / {item.capacity}\n"
            result += f"Type: {item.type}\n"
            software_list = [s.name for s in item.software_components]
            result += f"Software Components: {', '.join(software_list) if software_list else None}"
        return result
