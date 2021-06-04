#!/usr/bin/python3
"""Class that prints a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class that prints a rectangle"""

    def __init__(self, width, height, x=0, y=0, id = None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__height = value
    
    # X
       # height
    @property
    def x(self):
        return self.__height
    
    @X.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""

        return self.__width * self.__height
    
