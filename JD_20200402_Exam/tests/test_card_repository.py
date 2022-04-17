from unittest import TestCase, main

from project.card.trap_card import TrapCard
from project.card.card_repository import CardRepository


class TestCardRepository(TestCase):

    def setUp(self) -> None:
        self.test_repository = CardRepository()
        self.test_card = TrapCard("test_card")

    def test_initialization(self):
        self.assertEqual(0, self.test_repository.count)
        self.assertListEqual([], self.test_repository.cards)

    def test_add(self):
        self.test_repository.add(self.test_card)
        self.assertEqual(1, self.test_repository.count)
        self.assertListEqual([self.test_card], self.test_repository.cards)

    def test_add_same_player(self):
        self.test_repository.add(self.test_card)
        self.assertEqual(1, self.test_repository.count)
        self.assertListEqual([self.test_card], self.test_repository.cards)
        with self.assertRaises(ValueError) as context:
            self.test_repository.add(self.test_card)
        self.assertEqual(f"Card {self.test_card.name} already exists!", str(context.exception))

    def test_remove_invalid_username(self):
        invalid_name = ""
        with self.assertRaises(ValueError) as context:
            self.test_repository.remove(invalid_name)
        self.assertEqual("Card cannot be an empty string!", str(context.exception))

    def test_remove(self):
        self.test_repository.add(self.test_card)
        self.assertEqual(1, self.test_repository.count)
        self.assertListEqual([self.test_card], self.test_repository.cards)
        self.test_repository.remove("test_card")
        self.assertEqual(0, self.test_repository.count)
        self.assertListEqual([], self.test_repository.cards)

    def test_find(self):
        self.test_repository.add(self.test_card)
        self.assertEqual(self.test_card, self.test_repository.find("test_card"))


if __name__ == "__main__":
    main()
