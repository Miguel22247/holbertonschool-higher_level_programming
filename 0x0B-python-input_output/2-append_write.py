#!/usr/bin/python3
"""append a string at the end of a file"""


def append_write(filename="", text=""):
	with open(filename, mode = "a", enconding="utf-8") as appendFile:
		appendFile.write(text)
		return len(text)
