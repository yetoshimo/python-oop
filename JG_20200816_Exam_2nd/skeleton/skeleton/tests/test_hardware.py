from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(TestCase):

    def setUp(self) -> None:
        self.test_hardware = Hardware("test", "Heavy", 200, 100)

    def test_initialization(self):
        self.assertEqual("test", self.test_hardware.name)
        self.assertEqual("Heavy", self.test_hardware.type)
        self.assertEqual(200, self.test_hardware.capacity)
        self.assertEqual(100, self.test_hardware.memory)
        self.assertListEqual([], self.test_hardware.software_components)

    def test_install_invalid_memory(self):
        es = ExpressSoftware("test", 100, 100)
        with self.assertRaises(Exception) as context:
            self.test_hardware.install(es)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_install_invalid_capacity(self):
        es = ExpressSoftware("test", 300, 50)
        with self.assertRaises(Exception) as context:
            self.test_hardware.install(es)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_install_valid_software(self):
        es = ExpressSoftware("test", 100, 50)
        self.test_hardware.install(es)
        self.assertListEqual([es], self.test_hardware.software_components)

    def test_uninstall_valid_software(self):
        es = ExpressSoftware("test", 100, 50)
        self.test_hardware.install(es)
        self.assertListEqual([es], self.test_hardware.software_components)
        self.test_hardware.uninstall(es)
        self.assertListEqual([], self.test_hardware.software_components)


if __name__ == "__main__":
    main()
