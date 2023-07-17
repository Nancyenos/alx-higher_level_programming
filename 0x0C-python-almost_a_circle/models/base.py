#!/usr/bin/python3

""" This class will be the “base” of all other classes in this project. """
import json


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
    @staticmethod        
    def to_json_string(list_dictionaries):
        """ return the Json string of a dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json strings of a list to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ method to change json string to list """
        if  json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)
