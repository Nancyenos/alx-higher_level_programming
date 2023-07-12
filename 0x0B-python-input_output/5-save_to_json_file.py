#!/usr/bin/python3
"""Defines a JSON  function to write files."""
import json


def save_to_json_file(my_obj, filename):
    """function that writes object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
