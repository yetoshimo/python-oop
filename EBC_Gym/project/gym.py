class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def check_customer(_customer, _customers):
        return _customer in _customers

    @staticmethod
    def check_trainer(_trainer, _trainers):
        return _trainer in _trainers

    @staticmethod
    def check_equipment(_equipment, _equipments):
        return _equipment in _equipments

    @staticmethod
    def check_plan(_plan, _plans):
        return _plan in _plans

    @staticmethod
    def check_subscription(_subscription, _subscriptions):
        return _subscription in _subscriptions

    def add_customer(self, customer):
        if not self.check_customer(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not self.check_trainer(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not self.check_equipment(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not self.check_plan(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not self.check_subscription(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        _get_subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions))
        _get_customer = next(filter(lambda x: x.id == _get_subscription.customer_id, self.customers))
        _get_trainer = next(filter(lambda x: x.id == _get_subscription.trainer_id, self.trainers))
        _get_plan = next(filter(lambda x: x.id == _get_subscription.exercise_id, self.plans))
        _get_equipment = next(filter(lambda x: x.id == _get_plan.equipment_id, self.equipment))
        return repr(_get_subscription) + '\n' + \
               repr(_get_customer) + '\n' + \
               repr(_get_trainer) + '\n' + \
               repr(_get_equipment) + '\n' + \
               repr(_get_plan)
