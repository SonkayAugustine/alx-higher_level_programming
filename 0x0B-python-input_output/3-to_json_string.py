#!/usr/bin/python3
"""
Task 3 module
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)"""
    s = json.dumps(my_obj)
    return (s)
