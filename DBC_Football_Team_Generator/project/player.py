class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.name}\n" \
               f"Sprint: {self.sprint}\n" \
               f"Dribble: {self.dribble}\n" \
               f"Passing: {self.passing}\n" \
               f"Shooting: {self.shooting}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        pass

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value
        pass

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value
        pass

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value
        pass

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value
        pass
