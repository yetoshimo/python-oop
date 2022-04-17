from project.table.table import Table


class InsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @staticmethod
    def __validate_table_number(value):
        if not 1 <= value <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self._table_number = value
