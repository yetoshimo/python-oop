from unittest import TestCase, main

from project.appliances.laptop import Laptop
from project.rooms.room import Room


class TestRoom(TestCase):

    def setUp(self) -> None:
        self.test_room = Room("test", 100, 2)

    def test_initialization(self):
        self.assertEqual("test", self.test_room.family_name)
        self.assertEqual(100, self.test_room.budget)
        self.assertEqual(2, self.test_room.members_count)
        self.assertEqual(0, self.test_room.expenses)
        self.assertListEqual([], self.test_room.children)

    def test_set_expenses_invalid_value(self):
        with self.assertRaises(ValueError) as context:
            self.test_room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(context.exception))

    def test_set_expenses_valid_value(self):
        self.test_room.expenses = 200
        self.assertEqual(200, self.test_room.expenses)

    def test_calculate_expenses(self):
        self.test_room.calculate_expenses([Laptop()])
        self.assertEqual(30, self.test_room.expenses)


if __name__ == "__main__":
    main()
