#!/usr/bin/python3
import json
"""
Module: 5-to_json_string.py
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)"""
    s = json.dumps(my_obj)
    return (s)
