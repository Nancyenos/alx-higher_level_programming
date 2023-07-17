#!/usr/bin/python3
""" Defines a square that inherits from rectangle """

from models.rectangle import Rectangle

class Square(Rectangle):
    """" A square from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square """
        super().__init__(size, size, x, y , id)

    @property
    def size(self):
        """ gets size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets property of size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the rectangle with key and positional args
        args:width(int)
             height(int)
             x(int)
             y (int)
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.size = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]

        if args:
            kwargs = {}

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.size = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """ return dictionary represantion of square """
        return{
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """" string represantion of square """
        return("[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.height))
