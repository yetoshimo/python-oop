from project.card.card import Card


class MagicCard(Card):
    default_damage_points = 5
    default_health_points = 80

    def __init__(self, name: str):
        super().__init__(name, MagicCard.default_damage_points, MagicCard.default_health_points)
