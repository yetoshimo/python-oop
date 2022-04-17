from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(TestCase):

    def setUp(self) -> None:
        self.test_hardware = Hardware("test", "Power", 100, 200)

    def test_initialization(self):
        self.assertEqual("test", self.test_hardware.name)
        self.assertEqual("Power", self.test_hardware.type)
        self.assertEqual(100, self.test_hardware.capacity)
        self.assertEqual(200, self.test_hardware.memory)
        self.assertListEqual([], self.test_hardware.software_components)

    def test_install_invalid_software_memory(self):
        test_software = ExpressSoftware("test", 75, 150)
        with self.assertRaises(Exception) as context:
            self.test_hardware.install(test_software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_install_invalid_software_capacity(self):
        test_software = ExpressSoftware("test", 150, 25)
        with self.assertRaises(Exception) as context:
            self.test_hardware.install(test_software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_install_software(self):
        test_software = ExpressSoftware("test", 75, 25)
        self.test_hardware.install(test_software)
        self.assertListEqual([test_software], self.test_hardware.software_components)
        self.assertEqual(test_software.memory_consumption, self.test_hardware.used_memory)
        self.assertEqual(test_software.capacity_consumption, self.test_hardware.used_capacity)

    def test_uninstall_software(self):
        test_software = ExpressSoftware("test", 75, 25)
        self.test_hardware.install(test_software)
        self.assertListEqual([test_software], self.test_hardware.software_components)
        self.test_hardware.uninstall(test_software)
        self.assertListEqual([], self.test_hardware.software_components)


if __name__ == "__main__":
    main()
