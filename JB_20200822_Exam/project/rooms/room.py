class Room:
    room_cost = 0
    appliances = []

    def __init__(self, name: str, budget: float, members_count: int):
        self.members_count = members_count
        self.budget = budget
        self.family_name = name
        self.children: list = []
        self.expenses = 0

    @staticmethod
    def __check_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        self.__check_expenses(value)
        self._expenses = value

    @property
    def total_room_cost(self):
        return self.expenses + self.room_cost

    @property
    def appliances_cost(self):
        return sum(a.get_monthly_expense() for a in self.appliances)

    def calculate_expenses(self, *args):
        _result = 0
        _result += sum(e.get_monthly_expense() for item in args for e in item)
        self.expenses = _result

    def __repr__(self):
        room_result = ""
        room_result += f"{self.family_name} with {self.members_count} members. " \
                       f"Budget: {self.budget:.2f}$, Expenses: {self.total_room_cost:.2f}$\n"
        if self.children:
            for index, child in enumerate(self.children):
                room_result += f"--- Child {index + 1} monthly cost: {child.get_monthly_expense():.2f}$\n"
        room_result += f"--- Appliances monthly cost: {self.appliances_cost:.2f}$"
        return room_result
