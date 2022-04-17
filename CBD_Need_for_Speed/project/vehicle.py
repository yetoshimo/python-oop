class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.get_fuel_consumption

    @property
    def get_fuel_consumption(self):
        return self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if self.fuel_consumption * kilometers <= self.fuel:
            self.fuel -= float(self.fuel_consumption * kilometers)
