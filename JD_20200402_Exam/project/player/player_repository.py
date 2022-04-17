from project.player.player import Player


class PlayerRepository:

    def __init__(self):
        self.count: int = 0
        self.players: list = []

    @staticmethod
    def __check_player_string(value):
        if value == "" or value is None:
            raise ValueError("Player cannot be an empty string!")

    def __check_player(self, player):
        try:
            player_to_add = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except IndexError:
            pass

    def add(self, player: Player):
        self.__check_player(player)
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        self.__check_player_string(player)
        player_to_remove = [p for p in self.players if p.username == player][0]
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username: str):
        return [p for p in self.players if p.username == username][0]
