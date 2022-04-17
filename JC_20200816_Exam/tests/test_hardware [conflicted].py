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
        # self.assertEqual("Software cannot be installed", str(context))


if __name__ == "__main__":
    main()
