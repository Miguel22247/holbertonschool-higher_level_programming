#!/usr/bin/python3
"""Class base"""
import json


class Base:
	"""Base class for other shapes"""
	__nb_objects = 0

	def __init__(self, id=None):
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

