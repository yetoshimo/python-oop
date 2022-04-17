from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.test_library = Library("test_library")

    def test_initialization(self):
        self.assertEqual("test_library", self.test_library.name)
        self.assertDictEqual({}, self.test_library.books_by_authors)
        self.assertDictEqual({}, self.test_library.readers)

    def test_initialization_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Library("")
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book(self):
        self.test_library.add_book("test_author", "test_title")
        self.assertDictEqual({"test_author": ["test_title"]}, self.test_library.books_by_authors)

    def test_add_reader_valid_name(self):
        self.test_library.add_reader("test_reader")
        self.assertDictEqual({"test_reader": []}, self.test_library.readers)

    def test_add_reader_invalid_name(self):
        self.test_library.add_reader("test_reader")
        self.assertDictEqual({"test_reader": []}, self.test_library.readers)
        self.assertEqual("test_reader is already registered in the test_library library.",
                         self.test_library.add_reader("test_reader"))

    def test_rent_book_invalid_reader(self):
        self.test_library.add_book("test_author", "test_title")
        self.test_library.add_reader("test_reader1")
        self.assertEqual("test_reader is not registered in the test_library Library.",
                         self.test_library.rent_book("test_reader", "test_author", "test_title"))

    def test_rent_book_invalid_author(self):
        self.test_library.add_book("test_author", "test_title")
        self.test_library.add_reader("test_reader")
        self.assertEqual("test_library Library does not have any test_author1's books.",
                         self.test_library.rent_book("test_reader", "test_author1", "test_title"))

    def test_rent_book_invalid_title(self):
        self.test_library.add_book("test_author", "test_title")
        self.test_library.add_reader("test_reader")
        self.assertEqual("""test_library Library does not have test_author's "test_title1".""",
                         self.test_library.rent_book("test_reader", "test_author", "test_title1"))

    def test_rent_book_valid(self):
        self.test_library.add_book("test_author", "test_title")
        self.test_library.add_reader("test_reader")
        self.test_library.rent_book("test_reader", "test_author", "test_title")
        self.assertDictEqual({"test_reader": [{"test_author": "test_title"}]}, self.test_library.readers)
        self.assertDictEqual({"test_author": []}, self.test_library.books_by_authors)


if __name__ == "__main__":
    main()
