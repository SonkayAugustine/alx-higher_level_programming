#!/usr/bin/python3
"""
task module: 11-student.py
"""


class Student:
    """student class"""
    def __init__(self, first_name. last_name, age):
        """Initialization of the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """return a dictionary representation of a student instance
            Only attribute names contained
in this list must be retrieved.
            Otherwise, all attributes must be retrieved
"""

            try:
                for attr in attrs:
                    if type(attr) is not str:
                        return self.__dict__
            except Exception:
                return self.__dict__
            my_dict = dict()
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict

        def reload_from_json(self, json):
            """this function replaces all attributes of the Student instance
            with the ones in the json argument
            """
            for key, value in json.items():
                setattr(self, key, value)
