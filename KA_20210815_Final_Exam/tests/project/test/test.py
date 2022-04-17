from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.test_pet_shop = PetShop("test")

    def test_initialization(self):
        self.assertEqual("test", self.test_pet_shop.name)
        self.assertDictEqual({}, self.test_pet_shop.food)
        self.assertListEqual([], self.test_pet_shop.pets)

    def test_add_food_invalid_quantity(self):
        with self.assertRaises(ValueError) as context:
            self.test_pet_shop.add_food("test_food", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(context.exception))

    def test_add_food_valid(self):
        self.assertDictEqual({}, self.test_pet_shop.food)
        self.assertEqual(f"Successfully added 10.00 grams of test_food.",
                         self.test_pet_shop.add_food("test_food", 10))
        self.assertDictEqual({"test_food": 10}, self.test_pet_shop.food)

    def test_add_food_existing_food(self):
        self.assertDictEqual({}, self.test_pet_shop.food)
        self.assertEqual(f"Successfully added 10.00 grams of test_food.",
                         self.test_pet_shop.add_food("test_food", 10))
        self.assertDictEqual({"test_food": 10}, self.test_pet_shop.food)
        self.assertEqual(f"Successfully added 10.00 grams of test_food.",
                         self.test_pet_shop.add_food("test_food", 10))
        self.assertDictEqual({"test_food": 20}, self.test_pet_shop.food)

    def test_add_pet_existing_name(self):
        self.test_pet_shop.add_pet("test_pet")
        self.assertListEqual(["test_pet"], self.test_pet_shop.pets)
        with self.assertRaises(Exception) as context:
            self.test_pet_shop.add_pet("test_pet")
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_add_pet(self):
        self.assertEqual("Successfully added test_pet.", self.test_pet_shop.add_pet("test_pet"))
        self.assertListEqual(["test_pet"], self.test_pet_shop.pets)

    def test_feed_pet_invalid_pet(self):
        with self.assertRaises(Exception) as context:
            self.test_pet_shop.feed_pet("test_food", "test_pet")
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet_invalid_food(self):
        self.test_pet_shop.add_pet("test_pet")
        self.assertListEqual(["test_pet"], self.test_pet_shop.pets)
        self.assertEqual("You do not have test_food", self.test_pet_shop.feed_pet("test_food", "test_pet"))

    def test_feed_pet_valid_entry(self):
        self.test_pet_shop.add_pet("test_pet")
        self.test_pet_shop.add_food("test_food", 50)
        self.assertEqual("Adding food...", self.test_pet_shop.feed_pet("test_food", "test_pet"))
        self.assertDictEqual({"test_food": 1050}, self.test_pet_shop.food)
        self.assertEqual("test_pet was successfully fed", self.test_pet_shop.feed_pet("test_food", "test_pet"))
        self.assertDictEqual({"test_food": 950}, self.test_pet_shop.food)

    def test_repr(self):
        self.test_pet_shop.add_pet("test_pet")
        self.test_pet_shop.add_pet("test_pet_2")
        self.test_pet_shop.add_food("test_food", 100)
        self.assertEqual("Shop test:\nPets: test_pet, test_pet_2", str(self.test_pet_shop))


if __name__ == "__main__":
    main()
