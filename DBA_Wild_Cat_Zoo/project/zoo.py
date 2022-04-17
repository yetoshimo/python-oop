class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    @staticmethod
    def __is_space_enough(_current_cap, _total_cap):
        return _current_cap < _total_cap

    @staticmethod
    def __can_hire_worker(_current_cap, _total_cap):
        return _current_cap < _total_cap

    @staticmethod
    def __is_worker_hired(_worker_name, _workers):
        return _worker_name in [i.name for i in _workers]

    @staticmethod
    def __can_pay_action(_total_needed, _budget):
        return _total_needed <= _budget

    def add_animal(self, animal, price):
        if not self.__is_space_enough(len(self.animals), self.__animal_capacity):
            return f"Not enough space for animal"

        if self.__is_space_enough(len(self.animals), self.__animal_capacity) \
                and not self.__can_pay_action(price, self.__budget):
            return f"Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.__can_hire_worker(len(self.workers), self.__workers_capacity):
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        if not self.__is_worker_hired(worker_name, self.workers):
            return f"There is no {worker_name} in the zoo"

        _worker_to_remove = next(filter(lambda x: x.name == worker_name, self.workers))
        self.workers.remove(_worker_to_remove)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        _needed_budget = sum(list(map(lambda x: x.salary, self.workers)))
        if not self.__can_pay_action(_needed_budget, self.__budget):
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= _needed_budget
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        _needed_budget = sum(list(map(lambda x: x.get_needs(), self.animals)))
        if not self.__can_pay_action(_needed_budget, self.__budget):
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= _needed_budget
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        _lions = list(filter(lambda x: x.__class__.__name__ == "Lion", self.animals))
        _tigers = list(filter(lambda x: x.__class__.__name__ == "Tiger", self.animals))
        _cheetahs = list(filter(lambda x: x.__class__.__name__ == "Cheetah", self.animals))

        _return = f"You have {len(self.animals)} animals\n"

        _return += f"----- {len(_lions)} Lions:\n"

        _return += '\n'.join([repr(_lion) for _lion in _lions]) + '\n'

        _return += f"----- {len(_tigers)} Tigers:\n"

        _return += '\n'.join([repr(_tiger) for _tiger in _tigers]) + '\n'

        _return += f"----- {len(_cheetahs)} Cheetahs:\n"

        _return += '\n'.join([repr(_cheetah) for _cheetah in _cheetahs])

        return _return

    def workers_status(self):
        _keepers = list(filter(lambda x: x.__class__.__name__ == "Keeper", self.workers))
        _caretakers = list(filter(lambda x: x.__class__.__name__ == "Caretaker", self.workers))
        _vets = list(filter(lambda x: x.__class__.__name__ == "Vet", self.workers))

        _return = f"You have {len(self.workers)} workers\n"

        _return += f"----- {len(_keepers)} Keepers:\n"

        _return += '\n'.join([repr(_keeper) for _keeper in _keepers]) + '\n'

        _return += f"----- {len(_caretakers)} Caretakers:\n"

        _return += '\n'.join([repr(_caretaker) for _caretaker in _caretakers]) + '\n'

        _return += f"----- {len(_vets)} Vets:\n"

        _return += '\n'.join([repr(_vet) for _vet in _vets])

        return _return
