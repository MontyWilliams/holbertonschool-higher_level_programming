#!/usr/bin/python3
"""base class
"""
import json
import os

class Base:
    """this is the base class that all others will inherit from
    __nb_objects is a private attribute that gives an i.d to 
    an obj that dosnt have 1

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """this initiates the obj
        """
        if id is None:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
                """returns a JSON string representation of a dictionary
                """
                if not list_dictionaries:
                    return "[]"
                return json.dumps(list_dictionaries)    
        
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of an object
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of the JSON string, 'json_string'.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method returns an object with the attributes
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        if cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """return a list of instances of a class
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            newlist = cls.from_json_string(file.read())
        newobj = []
        for dict in newlist:
            newobj.append(cls.create(**dict))
        return newobj 

    @classmethod
    def clear_Id(self):
        """ this method clears the id and is used for testing
        """
        Base.__nb_objects = 0

