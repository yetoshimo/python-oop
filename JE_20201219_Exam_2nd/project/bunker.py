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
        food_items = [i for i in self.supplies if i.__class__.__name__ == "FoodSupply"]
        if food_items:
            return food_items
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water_items = [i for i in self.supplies if i.__class__.__name__ == "WaterSupply"]
        if water_items:
            return water_items
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkiller_items = [i for i in self.medicine if i.__class__.__name__ == "Painkiller"]
        if painkiller_items:
            return painkiller_items
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salve_items = [i for i in self.medicine if i.__class__.__name__ == "Salve"]
        if salve_items:
            return salve_items
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

    def __decrease_needs(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

    def __sustain_survivors(self):
        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")

    def next_day(self):
        self.__decrease_needs()
        self.__sustain_survivors()
