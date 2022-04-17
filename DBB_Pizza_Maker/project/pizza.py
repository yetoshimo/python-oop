class Pizza:

    def __init__(self, name: str, dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}  # topping type as a key and the topping's weight as a value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        if not _name:
            raise ValueError(f"The name cannot be an empty string")
        self.__name = _name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, _dough):
        if not _dough:
            raise ValueError(f"You should add dough to the pizza")
        self.__dough = _dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, _toppings_capacity):
        if _toppings_capacity <= 0:
            raise ValueError(f"The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = _toppings_capacity

    @staticmethod
    def __is_capacity_enough(_current_toppings, _total_capacity):
        return len(_current_toppings) < _total_capacity

    def add_topping(self, topping):
        if not self.__is_capacity_enough(self.toppings, self.__toppings_capacity):
            raise ValueError(f"Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return sum([i for i in self.toppings.values()]) + self.dough.weight
