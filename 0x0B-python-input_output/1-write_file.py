#!/usr/bin/python3
"""Function that write a file on UTF-8"""


def write_file(filename="", text=""):

    with open(filename, mode="w", enconding="utf-8") as writeFile:
        return writeFile.write(text)
