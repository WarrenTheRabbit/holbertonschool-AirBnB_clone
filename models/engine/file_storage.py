#!/usr/bin/python3
"""module containing the class FileStorage"""
import json
import os
import models


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

    def new(self, obj):
        """
        Sets obj into __objects
        following the following format
        key: "<class name>.<instance id>"
        value: dictionary with obj attributes
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.objects.update({key: obj})

    def save(self):
        """serializes (converts the objects in) __objects to the JSON file"""
        json_string = json.dumps(self.objects, 
                                 default=lambda x: x.to_dict())
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json_string)

    def get_class(self, value: dict) -> models.BaseModel:
        """return the Class object of an instance persisted in JSON format"""
        return eval(f"models.{value['__class__']}")

    def reload(self):
        """deserializes (creates objects from) the JSON file and stores them
        in objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj_dicts = json.load(f)
                for key, value in obj_dicts.items():
                    Cls = self.get_class(value)
                    obj = Cls(**value)
                    self.objects.update({key: obj})
