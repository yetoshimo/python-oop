class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _year = int(date.split(".")[2])
        _month_number = int(date.split(".")[1])
        _months = {1: 'January',
                   2: 'February',
                   3: 'March',
                   4: 'April',
                   5: 'May',
                   6: 'June',
                   7: 'July',
                   8: 'August',
                   9: 'September',
                   10: 'October',
                   11: 'November',
                   12: 'December'}
        _month = _months[_month_number]
        return cls(name, id, _year, _month, age_restriction)
