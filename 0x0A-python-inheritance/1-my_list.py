#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
	"""prints the list sorted"""
	
	def print_sorted(self):

		if issubclass(MyList, list):
			print(sorted(list))
