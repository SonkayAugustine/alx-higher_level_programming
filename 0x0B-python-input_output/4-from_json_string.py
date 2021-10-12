#!/usr/bin/python3
"""
Module: 4-from_json_string.py
"""


import json


def from_json_string(my_obj):
    """Returns an object represented by a JSON string"""
    s = json.loads(my_obj)
    return (s)
