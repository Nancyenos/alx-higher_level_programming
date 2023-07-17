#!/usr/bin/python3

""" Defines a rectangle that inherits from Base """

from models.base import Base

class Rectangle(Base):
    """ a rectangle that inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes the rectangle """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width properties """
        if not isinstance(value, int): 
            """ If the input is not an integer,"""
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >  0")

        self.__width = value


    @property
    def height(self):
        """ Gets width """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting heights properties """
        if not isinstance(value, int):
            """ If the input is not an integer,"""
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >  0")
        self.__height = value
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            """ If the input is not an integer,"""
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=  0")
        self.__x = value
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            """ If the input is not an integer,"""
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >=  0")
        self.__y = value

    def area(self):
        """ calculates area of rectangle"""
        return self.width * self.height

    def display(self):
        """ prints rectangle with hashes in stdout"""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height))
