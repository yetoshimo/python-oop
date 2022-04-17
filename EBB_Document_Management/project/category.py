class Category:
    def __init__(self, id: int, name: str):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Category {self.id}: {self.name}"

    def edit(self, new_name: str):
        self.name = new_name