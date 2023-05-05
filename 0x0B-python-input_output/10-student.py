#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Represents the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_list = []
            for i in attrs:
                if i in self.__dict__:
                    new_list.append(i)
            return {x: self.__dict__[x] for x in new_list}
