from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            player_to_add = Beginner(username)
        else:
            player_to_add = Advanced(username)
        self.player_repository.add(player_to_add)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            card_to_add = MagicCard(name)
        else:
            card_to_add = TrapCard(name)
        self.card_repository.add(card_to_add)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        defender = self.player_repository.find(enemy_name)
        bf = BattleField()
        bf.fight(attacker, defender)
        return f"Attack user health {attacker.health} - Enemy user health {defender.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards {p.card_repository.count}\n"
            for c in p.card_repository.cards:
                result += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return result
