#!/usr/bin/python3
"""defines a lockedclass"""


class LockedClass:
    """
    cannot add attributes unless called first_name

    Attribute:
        first_name: string of first name
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """initiates new instances of Locked Class."""

        self.first_name = "first_name"
