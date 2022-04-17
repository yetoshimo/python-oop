from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        # name, mammal_type, sound
        self.test_mammal = Mammal("mammal_name", "mammal_type", "mammal_sound")

    def test_mammal_init(self):
        self.assertEqual("mammal_name", self.test_mammal.name)
        self.assertEqual("mammal_type", self.test_mammal.type)
        self.assertEqual("mammal_sound", self.test_mammal.sound)
        self.assertEqual("animals", self.test_mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        self.assertEqual(f"{self.test_mammal.name} makes {self.test_mammal.sound}", self.test_mammal.make_sound())

    def test_mammal_get_kingdom(self):
        self.assertEqual("animals", self.test_mammal.get_kingdom())

    def test_mammal_info(self):
        self.assertEqual(f"{self.test_mammal.name} is of type {self.test_mammal.type}", self.test_mammal.info())


if __name__ == "__main__":
    main()
