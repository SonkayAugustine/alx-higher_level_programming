#!/usr/bin/python3
"""
task module: 9-student.py
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary of student instance"""
        if self.__dict__:
            return self.__dict__
