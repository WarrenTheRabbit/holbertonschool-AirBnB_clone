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
        return self.objects

    def find(self, key):
        """returns the object with the given key or None if not found"""
        return self.objects.get(key, None)

    def new(self, obj):
        """
        Sets obj into __objects
        following the following format
        key: "<class name>.<instance id>"
        value: dictionary with obj attributes
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        to_save = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(to_save, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from utils import class_map

        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                obj_dicts = json.load(f)
                for value in obj_dicts.values():
                    Cls = class_map()[value["__class__"]]
                    obj = Cls(**value)
                    self.new(obj)
