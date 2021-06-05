#!/usr/bin/python3
"""class base"""
import json
import csv


class Base:
    """Base class of the other shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns JSON strings in list"""
        if type(json_string) != str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attrs already set"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        # update temp with obj func update()
        temp.update(**dictionary)
        return temp

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to file with JSON string"""
        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                # Using to_json_string(), and to_dictionary() to format
                write_file.write(cls.to_json_string(
                                 [item.to_dictionary() for item in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        # Converting str to list
        text = cls.from_json_string(text)
        for item in text:
            # Formatting dicts into str format
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return res
