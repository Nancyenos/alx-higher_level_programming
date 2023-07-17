#!/usr/bin/python3

""" This class will be the “base” of all other classes in this project. """

class Base:
    """ Base class to manae id to avid duplicates

     __nb_objects number of initialized ob

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ a new instance   
        args  = id -> id of new ob
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
