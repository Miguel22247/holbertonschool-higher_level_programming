#!/usr/bin/python3
"""function to create basegeometry"""


class BaseGeometry:
	"""class that contains function area"""

	def area(self):
		"""Function not implemented"""

        raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""Function not implemented"""

	if type(value) is not int:
		raise TypeError(name + "must be an integer")

	if value <= 0:
		raise ValueError(name + "must be greater than 0")
