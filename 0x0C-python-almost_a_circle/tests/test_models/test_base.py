#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_instance(unittest.TestCase):
    """ call to test all classes """
    def setUp(self):
        Base._Base_nb_objects = 0

    def test_idallocation(self):
        """ testing if id is allocated"""
        b1 = Base()
        b2= Base()
        b3 = Base(6)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 6)

    def test_dynamic_id_allocation(self):
        """ Check if the 'id' attribute exists and is different for each instance """
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertTrue(hasattr(b1, 'id'))
        self.assertTrue(hasattr(b2, 'id'))
        self.assertTrue(hasattr(b3, 'id'))
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_inheritance(self):
        """ Assume Rectangle and Square are subclasses of Base"""

        rect = Rectangle(10, 20)
        square = Square(5)

        self.assertTrue(isinstance(rect, Base))
        self.assertTrue(isinstance(square, Base))

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
if __name__ == "__main__":
    unittest.main()
