import unittest
from IA_Testing_Lab.test_cat import Cat


class CatTests(unittest.TestCase):

    cat_name = "Test Cat"

    def setUp(self):
        self.cat = Cat(self.cat_name)

    def test_cat_eat_size_is_increased_by_1(self):
        """Cat's size is increased after eating"""
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_cat_eat_is_fed_after_eating_is_true(self):
        """Cat is fed after eating"""
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_is_fed_raises_error(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.eat()

        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_fall_asleep_if_not_fed_raises_error(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_after_sleep(self):
        """Cat is not sleepy after sleeping"""
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
