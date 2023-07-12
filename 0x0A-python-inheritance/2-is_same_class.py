#!/usr/bin/python3
"""Defines a function to check a file."""


def is_same_class(obj, a_class):
    """unction that returns True if the object is exactly an instance of
    the specified class .

    Args:
        obj :object to check.
        a_class (type):class to compare obj
    Returns:
        If obj is exactly an instance of a_class - True.
        else- False.
    """
    if type(obj) == a_class:
        return True
    return False
