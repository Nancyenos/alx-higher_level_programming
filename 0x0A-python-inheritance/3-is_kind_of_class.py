#!/usr/bin/python3
"""Defines a sub class of funcyion to check obj"""


def is_kind_of_class(obj, a_class):
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
    if isinstance(obj, a_class):
        return True
    return False
