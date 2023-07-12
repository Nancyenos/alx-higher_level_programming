#!/usr/bin/python3
"""Defines a function that appends charter to files."""


def append_write(filename="", text=""):
    """Appends a str to the end of file.

    Args:
        filename (str): name of the file
        text (str): str to append to the file.
    Returns:
        count of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
