#!/usr/bin/python3
""" class Student."""


class Student:
    """class of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int):  age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a dictionary of the Student.

        reps only those attributes in the list.

        Args:
            attrs (list): attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance.

        Args:
            json (dict): value to replace
        """
        for k, v in json.items():
            setattr(self, k, v)
