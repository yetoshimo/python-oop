from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):

    def setUp(self) -> None:
        self.test_repository = PlayerRepository()
        self.test_player = Advanced("test_player")

    def test_initialization(self):
        self.assertEqual(0, self.test_repository.count)
        self.assertListEqual([], self.test_repository.players)

    def test_add(self):
        self.test_repository.add(self.test_player)
        self.assertEqual(1, self.test_repository.count)
        self.assertListEqual([self.test_player], self.test_repository.players)

    def test_add_same_player(self):
        self.test_repository.add(self.test_player)
        self.assertEqual(1, self.test_repository.count)
        self.assertListEqual([self.test_player], self.test_repository.players)
        with self.assertRaises(ValueError) as context:
            self.test_repository.add(self.test_player)
        self.assertEqual(f"Player {self.test_player.username} already exists!", str(context.exception))

    def test_remove_invalid_username(self):
        invalid_username = ""
        with self.assertRaises(ValueError) as context:
            self.test_repository.remove(invalid_username)
        self.assertEqual("Player cannot be an empty string!", str(context.exception))

    def test_remove(self):
        self.test_repository.add(self.test_player)
        self.assertEqual(1, self.test_repository.count)
        self.assertListEqual([self.test_player], self.test_repository.players)
        self.test_repository.remove("test_player")
        self.assertEqual(0, self.test_repository.count)
        self.assertListEqual([], self.test_repository.players)

    def test_find(self):
        self.test_repository.add(self.test_player)
        self.assertEqual(self.test_player, self.test_repository.find("test_player"))


if __name__ == "__main__":
    main()
