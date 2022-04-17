from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.test_vehicle = Vehicle(10, 100)

    def test_vehicle_init_values(self):
        self.assertEqual(10, self.test_vehicle.fuel)
        self.assertEqual(10, self.test_vehicle.capacity)
        self.assertEqual(100, self.test_vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.test_vehicle.fuel_consumption)

    def test_vehicle_fuel_capacity_does_not_change(self):
        self.assertEqual(10, self.test_vehicle.capacity)
        self.test_vehicle.fuel = 5
        self.assertEqual(10, self.test_vehicle.capacity)

    def test_vehicle_drive_expect_exception_when_fuel_needed_is_greater_than_fuel(self):
        with self.assertRaises(Exception) as context:
            self.test_vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_vehicle_drive_decreases_fuel_by_fuel_needed(self):
        # fuel_needed = self.fuel_consumption * kilometers
        self.test_vehicle.drive(5)
        self.assertEqual(3.75, self.test_vehicle.fuel)

    def test_vehicle_refuel_expect_exception_when_fuel_amount_and_available_fuel_is_greater_than_capacity(self):
        with self.assertRaises(Exception) as context:
            self.test_vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_vehicle_refuel_increases_fuel_amount(self):
        self.test_vehicle.drive(5)
        self.test_vehicle.refuel(1)
        self.assertEqual(4.75, self.test_vehicle.fuel)

    def test_vehicle_str_method(self):
        expected_message = f"The vehicle has {self.test_vehicle.horse_power} " \
                           f"horse power with {self.test_vehicle.fuel} fuel left " \
                           f"and {self.test_vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected_message, str(self.test_vehicle))


if __name__ == "__main__":
    main()
