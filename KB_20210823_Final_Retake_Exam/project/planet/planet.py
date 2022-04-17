class Planet:

    def __init__(self, name: str):
        self.name = name
        self.items: list = []

    @staticmethod
    def __validate_name(value):
        if value == "" or value.isspace():
            raise ValueError("Planet name cannot be empty string or whitespace!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self._name = value
