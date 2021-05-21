#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """Test the max int on ints"""
        self.assertEqual(max_integer(list=[0, 1, 2, 3]), 3)
        self.assertEqual(max_integer(list=[2, 3, 1, 0]), 3)
        self.assertEqual(max_integer(list=[-1000, 0, -4, -150]), 0)
        self.assertEqual(max_integer(list=[-100, -110, -400, -150]), -100)
        self.assertEqual(max_integer(list=[5, 5, 5]), 5)
        self.assertEqual(max_integer(list=[100.5, 100.4, 100.6]), 100.6)
        self.assertEqual(max_integer(list=[100.5, 100, 100.6]), 100.6)

    def test_empty(self):
        """Test if list is empty"""
        self.assertIsNone(max_integer(list=[None]))
        self.assertIsNone(max_integer(list=[]))
        self.assertIsNone(max_integer())

    def test_errors(self):
        """Test possible errors"""
        self.assertRaises(TypeError, max_integer, list=[2, "Hello", 3])
        self.assertRaises(TypeError, max_integer, list=[[1, 2, 3], 100, 100.6])
        self.assertRaises(TypeError, max_integer, list=[(1, 2), 100, 100.6])
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
