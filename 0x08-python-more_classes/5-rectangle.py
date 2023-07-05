#!/usr/bin/python3

""" defines a class of arectangle with height and width private """


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width: must be an int and <= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height: must be an integer and <= 0."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calcs the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """  should print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join("#" * self.__width for _ in range(self.__height)))

    def __repr__(self):
        """ should return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """print bye rectangle when an instance of the class is being deleted
        """
        print("Bye rectangle...")
