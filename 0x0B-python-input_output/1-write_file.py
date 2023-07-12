#!/usr/bin/python3
"""Defines a function that writes a file."""


def write_file(filename="", text=""):
    """Write a str to a U-T-F-8 file.

    Args:
        filename (str): The file to write.
        text (str): The text to write
    Returns:
        count of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
