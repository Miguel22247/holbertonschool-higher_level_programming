#!/usr/bin/python3
"""Function that read files on UTF-8"""


def read_file(filename=""):
    """Read the file on UTF-8"""


    with open(filename, enconding="utf-8") as readFile:
        print(readFile.read(), end="")
