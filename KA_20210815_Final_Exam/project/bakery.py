from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu: list = []
        self.drinks_menu: list = []
        self.tables_repository: list = []
        self.total_income = 0

    @staticmethod
    def __validate_name(value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self._name = value

    def __validate_food_name(self, food: BakedFood):
        try:
            f = [f for f in self.food_menu if f.name == food.name][0]
            # Test  #29 TODO RUNTIME
            raise Exception(f"{food.__class__.__name__} {food.name} is already in the menu!")
        except IndexError:
            pass

    def add_food(self, food_type: str, name: str, price: float):
        # try:
            if food_type == "Bread":
                f = Bread(name, price)
            else:
                f = Cake(name, price)
            self.__validate_food_name(f)
            self.food_menu.append(f)
            # Test  #30
            return f"Added {f.name} ({f.__class__.__name__}) to the food menu"
        # except ValueError:
        #     pass

    def __validate_drink_name(self, drink: Drink):
        try:
            d = [d for d in self.drinks_menu if d.name == drink.name][0]
            # Test  #31
            raise Exception(f"{drink.__class__.__name__} {drink.name} is already in the menu!")
        except IndexError:
            pass

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        # try:
            if drink_type == "Tea":
                d = Tea(name, portion, brand)
            else:
                d = Water(name, portion, brand)
            self.__validate_drink_name(d)
            self.drinks_menu.append(d)
            # Test  #32 TODO RUNTIME
            return f"Added {d.name} ({d.brand}) to the drink menu"
        # except ValueError:
        #     pass

    def __validate_table(self, table: Table):
        try:
            t = [t for t in self.tables_repository if t.table_number == table.table_number][0]
            # Test  #33
            raise Exception(f"Table {table.table_number} is already in the bakery!")
        except IndexError:
            pass

    def add_table(self, table_type: str, table_number: int, capacity: int):
        # try:
            if table_type == "InsideTable":
                t = InsideTable(table_number, capacity)
            else:
                t = OutsideTable(table_number, capacity)
            self.__validate_table(t)
            self.tables_repository.append(t)
            # Test  #34
            return f"Added table number {table_number} in the bakery"
        # except ValueError:
        #     pass

    def reserve_table(self, number_of_people: int):
        try:
            free_tables = [t for t in self.tables_repository if not t.is_reserved]
            t = [t for t in free_tables if t.capacity >= number_of_people][0]
            t.reserve(number_of_people)
            # Test  #35
            return f"Table {t.table_number} has been reserved for {number_of_people} people"
        except IndexError:
            # Test  #36
            return f"No available table for {number_of_people} people"

    # Test  #37
    def order_food(self, table_number: int, *args):
        not_in_menu_items = []
        try:
            t = [t for t in self.tables_repository if t.table_number == table_number][0]
            for food in args:
                if food in [f.name for f in self.food_menu]:
                    ordered_food = [f for f in self.food_menu if f.name == food][0]
                    t.order_food(ordered_food)
                else:
                    if len(not_in_menu_items) == 0:
                        not_in_menu_items.append(f"{self.name} does not have in the menu:")
                    not_in_menu_items.append(food)
            return '\n'.join(t.ordered_food + not_in_menu_items)
        # Test  #38
        except IndexError:
            return f"Could not find table {table_number}"

    # Test  #39
    def order_drink(self, table_number: int, *args):
        not_in_menu_items = []
        try:
            t = [t for t in self.tables_repository if t.table_number == table_number][0]
            for drink in args:
                if drink in [d.name for d in self.drinks_menu]:
                    ordered_drink = [f for f in self.drinks_menu if f.name == drink][0]
                    t.order_drink(ordered_drink)
                else:
                    if len(not_in_menu_items) == 0:
                        not_in_menu_items.append(f"{self.name} does not have in the menu:")
                    not_in_menu_items.append(drink)
            return '\n'.join(t.ordered_drinks + not_in_menu_items)
        # Test  #40
        except IndexError:
            return f"Could not find table {table_number}"

    # Test #41
    def leave_table(self, table_number: int):
        t = [t for t in self.tables_repository if t.table_number == table_number][0]
        tn = t.table_number
        bill = t.get_bill()
        self.total_income += bill
        t.clear()
        return f"Table: {tn}\nBill: {bill:.2f}"

    # Test #42
    def get_free_tables_info(self):
        free_tables = [t for t in self.tables_repository if not t.is_reserved]
        result = [info.free_table_info() for info in free_tables]
        return '\n'.join(result)

    # Test #43
    def get_total_income(self):
        # self.total_income = sum(t.get_bill() for t in self.tables_repository)
        return f"Total income: {self.total_income:.2f}lv"
