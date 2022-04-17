from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.list_of_players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        _temp_list_players = [p.name for p in self.list_of_players]
        if player_name in _temp_list_players:
            self.list_of_players.pop(_temp_list_players.index(player_name))
            return f"Player {player_name} has been removed from the guild."
        # else:
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        _guild_data = f"Guild: {self.name}\n"
        for p in self.list_of_players:
            _guild_data += p.player_info()
        return _guild_data


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
