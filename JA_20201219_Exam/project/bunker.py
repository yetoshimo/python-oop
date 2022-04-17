from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:

    def __init__(self):
        self.survivors: list = []
        self.supplies: list = []
        self.medicine: list = []

    @property
    def food(self):
        food_supplies = [i for i in self.supplies if i.__class__.__name__ == "FoodSupply"]
        if food_supplies:
            return food_supplies
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water_supplies = [i for i in self.supplies if i.__class__.__name__ == "WaterSupply"]
        if water_supplies:
            return water_supplies
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkiller_medicine = [i for i in self.medicine if i.__class__.__name__ == "Painkiller"]
        if painkiller_medicine:
            return painkiller_medicine
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salve_medicine = [i for i in self.medicine if i.__class__.__name__ == "Salve"]
        if salve_medicine:
            return salve_medicine
        raise IndexError("There are no salves left!")

    def __validate_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")

    def add_survivor(self, survivor: Survivor):
        self.__validate_survivor(survivor)
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                medicine_to_apply = self.painkillers.pop()
            else:
                medicine_to_apply = self.salves.pop()
            medicine_to_apply.apply(survivor)
            self.medicine.remove(medicine_to_apply)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                sustenance_to_apply = self.food.pop()
            else:
                sustenance_to_apply = self.water.pop()
            sustenance_to_apply.apply(survivor)
            self.supplies.remove(sustenance_to_apply)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def __decrease_survivors_needs(self):
        for s in self.survivors:
            s.needs -= s.age * 2

    def __sustain_survivors(self):
        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")

    def next_day(self):
        self.__decrease_survivors_needs()
        self.__sustain_survivors()
