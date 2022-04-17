from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    test_valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def setUp(self) -> None:
        self.test_paint_factory = PaintFactory("test", 1000)

    def test_initialization(self):
        self.assertEqual("test", self.test_paint_factory.name)
        self.assertEqual(1000, self.test_paint_factory.capacity)
        self.assertDictEqual({}, self.test_paint_factory.ingredients)
        self.assertListEqual(self.test_valid_ingredients, self.test_paint_factory.valid_ingredients)

    def test_add_ingredient_invalid_product_type(self):
        with self.assertRaises(TypeError) as context:
            self.test_paint_factory.add_ingredient("test", 100)
        self.assertEqual("Ingredient of type test not allowed in PaintFactory",
                         str(context.exception))

    def test_add_ingredient_invalid_capacity(self):
        with self.assertRaises(ValueError) as context:
            self.test_paint_factory.add_ingredient("white", 1001)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_ingredient_new_ingredients(self):
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertDictEqual({"white": 100}, self.test_paint_factory.ingredients)

    def test_add_ingredient_existing_ingredient(self):
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertDictEqual({"white": 100}, self.test_paint_factory.ingredients)
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertDictEqual({"white": 200}, self.test_paint_factory.ingredients)

    def test_remove_ingredient_invalid_ingredient(self):
        with self.assertRaises(KeyError) as context:
            self.test_paint_factory.remove_ingredient("test", 100)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_remove_ingredient_invalid_quantity(self):
        self.test_paint_factory.add_ingredient("white", 100)
        with self.assertRaises(ValueError) as context:
            self.test_paint_factory.remove_ingredient("white", 101)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_ingredient_decreases_quantity(self):
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertDictEqual({"white": 100}, self.test_paint_factory.ingredients)
        self.test_paint_factory.remove_ingredient("white", 50)
        self.assertDictEqual({"white": 50}, self.test_paint_factory.ingredients)

    def test_products(self):
        self.assertDictEqual({}, self.test_paint_factory.ingredients)


if __name__ == "__main__":
    main()
