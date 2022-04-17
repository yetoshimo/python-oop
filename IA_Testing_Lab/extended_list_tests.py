import unittest
from IA_Testing_Lab.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):

    def test_integer_list_add_when_item_is_integer(self):
        """add operation, should add an element and returns the list"""
        integer_list = IntegerList()
        internal_list = integer_list.add(1)

        self.assertEqual([1], internal_list)

    def test_integer_list_add_raises_value_error_when_item_is_not_integer(self):
        """If the element is not an integer, a ValueError is thrown"""
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add("Test")

    def test_integer_list_remove_index_removes_element_on_index_if_index_is_valid(self):
        """remove_index operation removes the element on that index and returns it"""
        value_to_be_removed = 3
        integer_list = IntegerList(1, 2, value_to_be_removed, 4)

        result = integer_list.remove_index(2)

        self.assertEqual(value_to_be_removed, result)
        # self.assertListEqual([1, 2, 4], integer_list.get_data())

    def test_integer_list_remove_index_raises_index_error_when_index_is_not_valid(self):
        """If the index is out of range, an IndexError is thrown"""
        integer_list = IntegerList(1, 2, 3, 4)
        index_to_be_removed = 4

        with self.assertRaises(IndexError):
            integer_list.remove_index(index_to_be_removed)

    def test_integer_list_init_takes_only_integers_and_stores_them(self):
        """__init__ should only take integers, and store them"""
        integer_list = IntegerList(1, 2, "Test", 4)
        self.assertEqual([1, 2, 4], integer_list.get_data())

    def test_integer_list_get_expect_specific_element_when_index_is_valid(self):
        """get should return the specific element"""
        expected_value = 3
        integer_list = IntegerList(1, 2, expected_value, 4)
        index = 2

        self.assertEqual(expected_value, integer_list.get(index))

    def test_integer_list_get_expect_index_error_when_index_is_invalid(self):
        """If the index is out of range, an IndexError is thrown"""
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.get(4)

    def test_integer_list_insert_expect_list_with_inserted_item(self):
        """Insert should place element in the list if the index and element type is valid"""
        integer_list = IntegerList(1, 2, 3, 4)
        integer_list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3, 4], integer_list.get_data())

    def test_integer_list_insert_expect_index_error_when_index_is_invalid(self):
        """If the index is out of range, IndexError is thrown"""
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.insert(4, 5)

    def test_integer_list_insert_expect_value_error_when_element_is_not_integer(self):
        """If the element is not an integer, ValueError is thrown"""
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            integer_list.insert(0, "Test")

    def test_integer_list_get_biggest_expect_max_element(self):
        """get_biggest returns the maximum value"""
        integer_list = IntegerList(1, 2, 3, 4)

        self.assertEqual(4, integer_list.get_biggest())

    def test_integer_list_get_index_expect_element_index(self):
        """get_index returns the index of the given element"""
        integer_list = IntegerList(1, 2, 3, 4)

        self.assertEqual(0, integer_list.get_index(1))


if __name__ == "__main__":
    unittest.main()
