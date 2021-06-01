#!/usr/bin/python3

"""Return True if the object is exactly an instance"""


def is_same_class(obj, a_class):

	if type(obj) is a_class:
		return True
	else:
		return False
