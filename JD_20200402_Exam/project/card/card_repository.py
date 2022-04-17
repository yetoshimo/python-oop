from project.card.card import Card


class CardRepository:

    def __init__(self):
        self.count: int = 0
        self.cards: list = []

    @staticmethod
    def __check_card_string(value):
        if value == "" or value is None:
            raise ValueError("Card cannot be an empty string!")

    def __check_card(self, card):
        try:
            card_to_add = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            pass

    def add(self, card: Card):
        self.__check_card(card)
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        self.__check_card_string(card)
        card_to_remove = [c for c in self.cards if c.name == card][0]
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name: str):
        return [c for c in self.cards if c.name == name][0]
