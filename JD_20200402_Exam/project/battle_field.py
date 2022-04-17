from project.player.player import Player


class BattleField:

    @staticmethod
    def __check_if_dead(player):
        if player.is_dead:
            raise ValueError("Player is dead!")

    @staticmethod
    def __increase_beginner_health_points(player):
        player.health += 40

    @staticmethod
    def __increase_beginner_damage_points(player):
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def __get_bonus_points(player):
        for card in player.card_repository.cards:
            player.health += card.health_points

    @staticmethod
    def __attack(attacker, enemy):
        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                return

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        BattleField.__check_if_dead(attacker)
        BattleField.__check_if_dead(enemy)
        if attacker.__class__.__name__ == "Beginner":
            BattleField.__increase_beginner_health_points(attacker)
            BattleField.__increase_beginner_damage_points(attacker)
        if enemy.__class__.__name__ == "Beginner":
            BattleField.__increase_beginner_health_points(enemy)
            BattleField.__increase_beginner_damage_points(enemy)
        BattleField.__get_bonus_points(attacker)
        BattleField.__get_bonus_points(enemy)
        BattleField.__attack(attacker, enemy)
        if not enemy.is_dead:
            BattleField.__attack(enemy, attacker)
