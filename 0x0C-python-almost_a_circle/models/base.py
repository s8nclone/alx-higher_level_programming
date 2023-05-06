#!/usr/bin/python3
"""This module contains the Base class which will be the
“base” of all other classes in this project.
"""
import json
import csv
import turtle


class Base():
    """This Base class will manage the id attribute for all classes

    Attributes:
        __nb_objects: the number of created Base objects.

    Arguments:
        @id: the id of a specific instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the default attributes of the Base object."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Arguments:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a class into a file.

        Arguments:
            list_objs (list): a list of objects.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation.

        Arguments:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set.

        Arguments:
            dictionary: the values of the wanted instance.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV string representation of a class into a file.

        Arguments:
            list_objs: a list of objects.
        """
        fields = []
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write('[]')
            else:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the CSV string representation of class from a file """
        fields = []
        try:
            with open(cls.__name__ + ".csv", 'r') as f:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in ln.items())
                        for ln in reader]
                return [cls.create(**dct) for dct in dcts]

        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles: a list of rectangle instances.
            list_squares: a list of square instances.
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
