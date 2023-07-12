#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a functin of an object reped by json str. """
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
