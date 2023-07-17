#!/usr/bin/python3
""" Defines a square that inherits from rectangle """

from models.rectangle import Rectangle

class Square(Rectangle):
    """" A square from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square """
        super().__init__(size, size, x, y , id)

    def __str__(self):
        """" string represantion of square """
        return("[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.height))
