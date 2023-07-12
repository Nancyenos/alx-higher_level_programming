#!/usr/bin/python3
"""Defines an inherited list"""


class MyList(list):
    """child class of list class that implements sorted list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
