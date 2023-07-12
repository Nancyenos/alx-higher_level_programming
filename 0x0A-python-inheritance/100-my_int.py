#!/usr/bin/python3
"""Defines a class that inherits from int."""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """function: != is =="""
        return self.real != value

    def __ne__(self, value):
        """function: == is !="""
        return self.real == value
