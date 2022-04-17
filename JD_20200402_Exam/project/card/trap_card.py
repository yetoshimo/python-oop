from project.card.card import Card


class TrapCard(Card):
    default_damage_points = 120
    default_health_points = 5

    def __init__(self, name: str):
        super().__init__(name, TrapCard.default_damage_points, TrapCard.default_health_points)
