#!/usr/bin/python3
"""Class that prints a rectangle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle Class constructor"""
        # Call the super class with id
        super().__init__(id)
        # Width:
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        # Height:
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        # X:
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        # Y:
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    # Getter and Setter for width
    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """checks the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    # Getter and Setter for height
    @property
    def height(self):
        """return for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """checks the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    # Getter and Setter for x
    @property
    def x(self):
        """return for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """checks the x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    # Getter and Setter for y
    @property
    def y(self):
        """return for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """checks the y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Calculates shape area"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with character '#'"""
        for a in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for b in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Override str function to return message"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)