class Room:
    room_cost = 0
    appliances = []
    default_members = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name: str = name
        self.budget: float = budget
        self.members_count: int = members_count
        self.children: list = []
        self.expenses = 0

    @staticmethod
    def __validate_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

    @property
    def total_room_cost(self):
        return self.expenses + self.room_cost

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self._expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum(element.get_monthly_expense() for item in args for element in item)

    def __repr__(self):
        _result = ""
        _result += f"{self.family_name} with {self.members_count} members. " \
                   f"Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$\n"
        if self.children:
            for index, child in enumerate(self.children):
                _result += f"--- Child {index + 1} monthly cost: {child.get_monthly_expense():.2f}$\n"
        _result += f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in self.appliances):.2f}$"
        return _result
