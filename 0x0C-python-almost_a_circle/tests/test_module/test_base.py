#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
import sys
import io
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingBase(unittest.TestCase):
    """class for Test Base"""

    # BASE CLASSES, TYPES, ARGUMENTS
    def test_base_repeated_id(self):
        """Base repeated ID"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(7)
        b4 = Base()
        b5 = Base(7)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 7)

    def test_base_types(self):
        """Base types"""
        Base._Base__nb_objects = 0
        self.assertEqual(str(type(Base)), "<class 'type'>")

        self.assertEqual(str(type(Rectangle)), "<class 'type'>")

        self.assertEqual(str(type(Square)), "<class 'type'>")

    def test_instance_Rectangle(self):
        """Is instance"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_instance_Square(self):
        """Is instance"""
        Base._Base__nb_objects = 0
        sq1 = Square(4)
        self.assertEqual(isinstance(sq1, Square), True)

    def test_type_instance_rectangle(self):
        """Same types"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        self.assertEqual(str(type(r1)), "<class 'models.rectangle.Rectangle'>")

    def test_type_instance_square(self):
        """Same types"""
        Base._Base__nb_objects = 0
        sq1 = Square(2)
        self.assertEqual(str(type(sq1)), "<class 'models.square.Square'>")

if __name__ == '__main__':
    unittest.main()
