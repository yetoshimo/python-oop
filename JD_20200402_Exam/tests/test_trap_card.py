from unittest import TestCase, main

from project.card.trap_card import TrapCard


class TestTrapCard(TestCase):

    def setUp(self):
        self.test_card = TrapCard("test_card")

    def test_initialization(self):
        self.assertEqual("test_card", self.test_card.name)
        self.assertEqual(5, self.test_card.health_points)
        self.assertEqual(120, self.test_card.damage_points)

    def test_invalid_name(self):
        invalid_name = ""
        with self.assertRaises(ValueError) as context:
            TrapCard(invalid_name)
        self.assertEqual("Card's name cannot be an empty string.", str(context.exception))

    def test_invalid_damage_points(self):
        invalid_damage_points = -1
        with self.assertRaises(ValueError) as context:
            self.test_card.damage_points = invalid_damage_points
        self.assertEqual("Card's damage points cannot be less than zero.", str(context.exception))

    def test_invalid_health_point(self):
        invalid_health_points = -1
        with self.assertRaises(ValueError) as context:
            self.test_card.health_points = invalid_health_points
        self.assertEqual("Card's HP cannot be less than zero.", str(context.exception))


if __name__ == "__main__":
    main()
