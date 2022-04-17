from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):

    def setUp(self):
        self.test_player = Advanced("test_player")

    def test_initialization(self):
        self.assertEqual(250, self.test_player.health)
        self.assertEqual("test_player", self.test_player.username)
        self.assertEqual("CardRepository", self.test_player.card_repository.__class__.__name__)
        self.assertFalse(self.test_player.is_dead)

    def test_invalid_username(self):
        invalid_username = ""
        with self.assertRaises(ValueError) as context:
            Advanced(invalid_username)
        self.assertEqual("Player's username cannot be an empty string.", str(context.exception))

    def test_invalid_health(self):
        invalid_health = -1
        with self.assertRaises(ValueError) as context:
            self.test_player.health = invalid_health
        self.assertEqual("Player's health bonus cannot be less than zero.", str(context.exception))

    def test_invalid_damage_points(self):
        invalid_damage_points = -1
        with self.assertRaises(ValueError) as context:
            self.test_player.take_damage(invalid_damage_points)
        self.assertEqual("Damage points cannot be less than zero.", str(context.exception))

    def test_take_damage_and_is_dead(self):
        self.assertFalse(self.test_player.is_dead)
        self.test_player.take_damage(50)
        self.assertEqual(200, self.test_player.health)
        self.test_player.take_damage(200)
        self.assertTrue(self.test_player.is_dead)


if __name__ == "__main__":
    main()
