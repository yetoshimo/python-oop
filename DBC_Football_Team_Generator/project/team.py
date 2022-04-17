class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        pass

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value
        pass

    @property
    def players(self):
        return self.__players

    def add_player(self, player):
        if player not in self.players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.name}"

        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        if player_name not in [i.name for i in self.players if i.name == player_name]:
            return f"Player {player_name} not found"

        _player_to_remove = next(filter(lambda x: x.name == player_name, self.players))
        self.__players.remove(_player_to_remove)
        return _player_to_remove
