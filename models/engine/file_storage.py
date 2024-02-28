#!/usr/bin/python3
"""module containing the class FileStorage"""
import json
import os


class FileStorage():
    """FileStorage class placeholder"""

    __file_path = "file.json"
    __objects = {}

    @property
    def objects(self):
        """Read the private objects dictionary"""
        return self.__objects

    @objects.setter
    def objects(self, updated_objects):
        """Modify the private class objects attribute"""
        self.__objects = updated_objects

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        Sets obj into __objects
        following the following format
        key: "<class name>.<instance id>"
        value: dictionary with obj attributes
        """
        key = obj.__class__.__name__ + "." + obj.id
        value = obj.to_dict()
        self.__objects.update({key: value})

    def save(self):
        """serializes __objects to the JSON file"""
        json_string = json.dumps(self.__objects)
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json_string)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                json_str = json.loads(f.read())
                for key, value in json_str.items():
                    self.__objects.update({key: value})
