from unittest import TestCase, main

from project.appliances.laptop import Laptop
from project.rooms.room import Room


class TestRoom(TestCase):

    def setUp(self) -> None:
        self.test_room = Room("test_room", 100, 2)

    def test_initialization(self):
        self.assertEqual("test_room", self.test_room.family_name)
        self.assertEqual(100, self.test_room.budget)
        self.assertEqual(2, self.test_room.members_count)
        self.assertListEqual([], self.test_room.children)
        self.assertEqual(0, self.test_room.expenses)

    def test_calculate_expenses(self):
        self.test_room.calculate_expenses(self.test_room.appliances)
        self.assertEqual(0, self.test_room.expenses)

    def test_set_expenses_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.test_room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(context.exception))

    def test_set_expenses_valid_value(self):
        self.test_room.expenses = 100
        self.assertEqual(100, self.test_room.expenses)

    def test_calculate_expenses_with_appliance(self):
        self.test_room.calculate_expenses([Laptop()])
        self.assertEqual(30, self.test_room.expenses)


if __name__ == "__main__":
    main()
