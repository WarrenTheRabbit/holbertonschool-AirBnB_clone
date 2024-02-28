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
        # value = obj.to_dict()
        # self.__objects.update({key: value})
        self.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        # json_string = json.dumps(self.__objects)
        to_save = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(to_save, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from utils import class_map
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                obj_dicts = json.load(f)
                for k, val in obj_dicts.items():
                    obj = class_map()[val["__class__"]](**val)
                    self.__objects.update({k: obj})
