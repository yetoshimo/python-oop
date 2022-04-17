class Dough:

    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, _flour_type):
        if not _flour_type:
            raise ValueError(f"The flour type cannot be an empty string")
        self.__flour_type = _flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, _baking_technique):
        if not _baking_technique:
            raise ValueError(f"The baking technique cannot be an empty string")
        self.__baking_technique = _baking_technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, _weight):
        if _weight <= 0:
            raise ValueError(f"The weight cannot be less or equal to zero")
        self.__weight = _weight
