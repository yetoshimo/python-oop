from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(TestCase):

    def setUp(self) -> None:
        self.test_battlefield = BattleField()
        self.test_attacker = Advanced("test_player")
        self.test_enemy = Beginner("test_player")

    def test_attacker_is_dead(self):
        self.test_attacker.health = 0
        with self.assertRaises(ValueError) as context:
            self.test_battlefield.fight(self.test_attacker, self.test_enemy)
        self.assertEqual("Player is dead!", str(context.exception))

    def test_enemy_is_dead(self):
        self.test_enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.test_battlefield.fight(self.test_attacker, self.test_enemy)
        self.assertEqual("Player is dead!", str(context.exception))

    def test_beginner_increase_health_points_damage_points(self):
        self.test_battlefield.fight(self.test_attacker, self.test_enemy)
        self.assertEqual(250, self.test_attacker.health)
        self.assertEqual(90, self.test_enemy.health)

    def test_attack(self):
        self.test_attacker.card_repository.add(MagicCard("test_card"))
        self.test_enemy.card_repository.add(TrapCard("test_card"))
        self.test_battlefield.fight(self.test_attacker, self.test_enemy)
        self.assertEqual(5, self.test_attacker.card_repository.find("test_card").damage_points)
        self.assertEqual(150, self.test_enemy.card_repository.find("test_card").damage_points)
        self.assertEqual(180, self.test_attacker.health)
        self.assertEqual(90, self.test_enemy.health)


if __name__ == "__main__":
    main()
