class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.id = id
        self.age = age
        self.name = name
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([i.name for i in self.rented_dvds])})"
