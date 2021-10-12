#!/usr/bin/python3
"""
task module: 6-load_from_json_file.py
"""


import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        my_object = json.load(f)
    return my_object
