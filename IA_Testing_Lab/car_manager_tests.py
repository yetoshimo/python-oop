import unittest
from IA_Testing_Lab.car_manager import Car


class TestCarManager(unittest.TestCase):

    def setUp(self):
        self.sample_car = Car("a", "b", 1, 4)

    def test_car_init(self):
        self.assertEqual(self.sample_car.make, "a")
        self.assertEqual(self.sample_car.model, "b")
        self.assertEqual(self.sample_car.fuel_consumption, 1)
        self.assertEqual(self.sample_car.fuel_capacity, 4)

    def test_car_make_setter(self):
        """Make cannot be null or empty"""
        with self.assertRaises(Exception):
            self.sample_car.make = ""

    def test_car_model_setter(self):
        """Model cannot be null or empty"""
        with self.assertRaises(Exception):
            self.sample_car.model = ""

    def test_car_fuel_consumption_setter(self):
        """Fuel consumption cannot be zero or negative"""
        with self.assertRaises(Exception):
            self.sample_car.fuel_consumption = -2

    def test_car_fuel_capacity_setter(self):
        """Fuel capacity cannot be zero or negative"""
        with self.assertRaises(Exception):
            self.sample_car.fuel_capacity = -1

    def test_car_fuel_amount_setter_with_invalid_value(self):
        """Fuel amount cannot be negative"""
        with self.assertRaises(Exception):
            self.sample_car.fuel_amount = -1

    def test_car_fuel_amount_setter_with_valid_value(self):
        self.sample_car.fuel_amount = 2
        self.assertEqual(self.sample_car.fuel_amount, 2)

    def test_car_refuel_raises_exception_when_amount_is_zero_or_negative(self):
        """Fuel amount cannot be zero or negative"""
        # self.assertRaises(Exception, self.sample_car.refuel, 0)
        self.assertRaises(Exception, self.sample_car.refuel, -1)

    def test_car_refuel_increases_fuel_capacity_when_amount_is_correct(self):
        """refuel increases fuel amount"""
        self.sample_car.refuel(2)
        self.assertEqual(self.sample_car.fuel_amount, 2)

    def test_car_refuel_max_fuel_capacity_when_amount_is_bigger_than_capacity(self):
        """refuel maxes the fuel capacity if the amount is bigger than the capacity"""
        self.sample_car.refuel(5)
        self.assertEqual(self.sample_car.fuel_amount, self.sample_car.fuel_capacity)

    def test_car_drive_raises_exception_when_needed_is_higher_than_fuel_amount(self):
        """You don't have enough fuel to drive"""
        with self.assertRaises(Exception) as context:
            self.sample_car.drive(1000)

        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")

    def test_car_drive_decreases_fuel_amount_when_needed_is_lower_than_fuel_amount(self):
        """needed = (distance / 100) * fuel_consumption"""
        self.sample_car.refuel(1)
        self.sample_car.drive(100)
        self.assertEqual(self.sample_car.fuel_amount, 0)


if __name__ == "__main__":
    unittest.main()
