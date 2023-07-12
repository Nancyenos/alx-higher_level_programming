#!/usr/bin/python3
"""Defines a sub class of funcyion to check obj"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj (any):object to check.
        a_class (type):class to compare  the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
