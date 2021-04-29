#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    for argument in range(1, len(argv)):
        result = result + int(argv[argument])
    print("{}".format(result))
