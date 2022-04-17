from unittest import TestCase, main

from project.controller import Controller


class TestController(TestCase):

    def setUp(self) -> None:
        self.test_controller = Controller()

    def test_initialization(self):
        self.assertEqual("PlayerRepository", self.test_controller.player_repository.__class__.__name__)
        self.assertEqual("CardRepository", self.test_controller.card_repository.__class__.__name__)
        self.assertListEqual([], self.test_controller.card_repository.cards)
        self.assertListEqual([], self.test_controller.player_repository.players)

    def test_add_player_beginner(self):
        result = self.test_controller.add_player("Beginner", "test_player")
        self.assertEqual(1, self.test_controller.player_repository.count)
        self.assertEqual("Beginner", self.test_controller.player_repository.find("test_player").__class__.__name__)
        self.assertEqual(result, f"Successfully added player of type Beginner with username: test_player")

    def test_add_player_advanced(self):
        result = self.test_controller.add_player("Advanced", "test_player")
        self.assertEqual(1, self.test_controller.player_repository.count)
        self.assertEqual("Advanced", self.test_controller.player_repository.find("test_player").__class__.__name__)
        self.assertEqual(result, f"Successfully added player of type Advanced with username: test_player")

    def test_add_card_magic(self):
        result = self.test_controller.add_card("Magic", "test_card")
        self.assertEqual(1, self.test_controller.card_repository.count)
        self.assertEqual("MagicCard", self.test_controller.card_repository.find("test_card").__class__.__name__)
        self.assertEqual(result, f"Successfully added card of type MagicCard with name: test_card")

    def test_add_card_trap(self):
        result = self.test_controller.add_card("Trap", "test_card")
        self.assertEqual(1, self.test_controller.card_repository.count)
        self.assertEqual("TrapCard", self.test_controller.card_repository.find("test_card").__class__.__name__)
        self.assertEqual(result, f"Successfully added card of type TrapCard with name: test_card")

    def test_add_player_card(self):
        self.test_controller.add_player("Beginner", "test_player")
        self.test_controller.add_card("Trap", "test_card")
        result = self.test_controller.add_player_card("test_player", "test_card")
        self.assertEqual(result, "Successfully added card: test_card to user: test_player")

    def test_fight(self):
        self.test_controller.add_player("Beginner", "test_player")
        self.test_controller.add_player("Advanced", "test_player_enemy")
        result = self.test_controller.fight("test_player", "test_player_enemy")
        attacker = self.test_controller.player_repository.find("test_player")
        defender = self.test_controller.player_repository.find("test_player_enemy")
        self.assertEqual(result, f"Attack user health {attacker.health} - Enemy user health {defender.health}")

    def test_report(self):
        self.test_controller.add_player("Beginner", "test_player")
        self.test_controller.add_card("Trap", "test_card")
        self.test_controller.add_player_card("test_player", "test_card")
        result = self.test_controller.report()
        expected = "Username: test_player - Health: 50 - Cards 1\n" \
                   "### Card: test_card - Damage: 120\n"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
