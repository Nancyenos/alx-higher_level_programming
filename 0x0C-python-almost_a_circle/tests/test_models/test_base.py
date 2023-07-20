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


if __name__ == "__main__":
    unittest.main()
