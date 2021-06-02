#!/usr/bin/python3
"""Function that write a file on UTF-8"""


def write_file(filename="", text=""):

    with open(filename, mode="w", enconding="utf-8") as writeFile:
        writeFile.write(text)
        return len(text)
