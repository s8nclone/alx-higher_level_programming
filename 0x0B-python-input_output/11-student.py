#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_list = []
            for i in attrs:
                if i in self.__dict__:
                    new_list.append(i)
            return {x: self.__dict__[x] for x in new_list}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for i, j in json.items():
            self.__dict__[i] = j
