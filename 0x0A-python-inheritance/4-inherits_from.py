#!/usr/bin/python3
"""Function that inherits"""


def inherits_from(obj, a_class):
    """Function that inherits"""

    if type(obj) is a_class:
        return True
    else:
        return isinstance(obj, a_class)
