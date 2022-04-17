class Survivor:
    max_health = 100
    max_needs = 100

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health: int = self.max_health
        self.needs: int = self.max_needs

    @staticmethod
    def __validate_name(value):
        if value == "" or value is None:
            raise ValueError("Name not valid!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self._name = value

    @staticmethod
    def __validate_age(value):
        if value < 0:
            raise ValueError("Age not valid!")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self._age = value

    @staticmethod
    def __validate_health(value):
        if value < 0:
            raise ValueError("Health not valid!")

    def __validate_max_health(self):
        if self._health > 100:
            self._health = self.max_health

    @property
    def health(self):
        self.__validate_max_health()
        return self._health

    @health.setter
    def health(self, value):
        self.__validate_health(value)
        self._health = value

    @staticmethod
    def __validate_needs(value):
        if value < 0:
            raise ValueError("Needs not valid!")

    def __validate_max_needs(self):
        if self._needs > 100:
            self._needs = self.max_needs

    @property
    def needs(self):
        self.__validate_max_needs()
        return self._needs

    @needs.setter
    def needs(self, value):
        self.__validate_needs(value)
        self._needs = value

    @property
    def needs_sustenance(self):
        return self.needs < self.max_needs

    @property
    def needs_healing(self):
        return self.health < self.max_health
