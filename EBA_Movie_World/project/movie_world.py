class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []  # list of Customer objects, empty upon initialization
        self.dvds = []  # list of DVD objects, empty upon initialization

    def __repr__(self):
        _customers = []
        _dvds = []

        for element in self.customers:
            _customers.append(f"{element.id}: {element.name} of age {element.age} has {len(element.rented_dvds)} rented DVD's ({''.join([i.name for i in element.rented_dvds])})")

        for element in self.dvds:
            _dvds.append(f"{element.id}: {element.name} ({element.creation_month} {element.creation_year}) has age restriction {element.age_restriction}. Status: {'rented' if element.is_rented else 'not rented'}")

        return '\n'.join(_customers) + '\n' + '\n'.join(_dvds)

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        _customer = next(filter(lambda x: x.id == customer_id, self.customers))
        _dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        if _dvd in _customer.rented_dvds:
            return f"{_customer.name} has already rented {_dvd.name}"
        if _dvd.is_rented:
            return f"DVD is already rented"
        if _customer.age < _dvd.age_restriction:
            return f"{_customer.name} should be at least {_dvd.age_restriction} to rent this movie"
        _customer.rented_dvds.append(_dvd)
        _dvd.is_rented = True
        return f"{_customer.name} has successfully rented {_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        _customer = next(filter(lambda x: x.id == customer_id, self.customers))
        _dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        if _dvd in _customer.rented_dvds:
            _customer.rented_dvds.remove(_dvd)
            _dvd.is_rented = False
            return f"{_customer.name} has successfully returned {_dvd.name}"
        return f"{_customer.name} does not have that DVD"
