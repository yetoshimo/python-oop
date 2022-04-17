from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        # username, level, health, damage
        self.test_hero = Hero("test_hero", 1, 100.1, 10.1)
        self.enemy_hero = Hero("enemy_hero", 1, 100.1, 10.1)

    def test_hero_init(self):
        self.assertEqual("test_hero", self.test_hero.username)
        self.assertEqual(1, self.test_hero.level)
        self.assertEqual(100.1, self.test_hero.health)
        self.assertEqual(10.1, self.test_hero.damage)

    def test_hero_battle_expect_exception_when_enemy_name_equals_username(self):
        self.enemy_hero.username = "test_hero"
        with self.assertRaises(Exception) as context:
            self.test_hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_battle_except_value_error_when_user_health_is_zero(self):
        self.test_hero.health = 0

        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle_except_value_error_when_user_health_is_lower_than_zero(self):
        self.test_hero.health = -1

        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle_except_value_error_when_enemy_health_is_zero(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(context.exception))

    def test_hero_battle_except_value_error_when_enemy_health_is_lower_than_zero(self):
        self.enemy_hero.health = -1

        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(context.exception))

    def test_hero_battle_player_loses(self):
        # player loses
        # player_damage = self.damage * self.level
        self.test_hero.level = 3
        self.assertEqual("You lose", self.test_hero.battle(self.enemy_hero))
        # self.test_hero.battle(self.enemy_hero)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(74.8, self.enemy_hero.health)
        self.assertEqual(15.1, self.enemy_hero.damage)

    def test_hero_battle_results_in_draw(self):
        self.test_hero.level = 10
        self.enemy_hero.level = 10
        self.assertEqual("Draw", self.test_hero.battle(self.enemy_hero))

    def test_hero_battle_player_wins(self):
        self.test_hero.level = 10
        # self.test_hero.battle(self.enemy_hero)
        self.assertEqual("You win", self.test_hero.battle(self.enemy_hero))
        self.assertEqual(11, self.test_hero.level)
        self.assertEqual(95, self.test_hero.health)
        self.assertEqual(15.1, self.test_hero.damage)

    def test_hero_returns_correct_str(self):
        expected_string = f"Hero {self.test_hero.username}: {self.test_hero.level} lvl\n" \
                          f"Health: {self.test_hero.health}\n" \
                          f"Damage: {self.test_hero.damage}\n"

        actual_string = str(self.test_hero)

        self.assertEqual(expected_string, actual_string)


if __name__ == "__main__":
    main()
