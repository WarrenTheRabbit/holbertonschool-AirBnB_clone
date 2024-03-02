#!/usr/bin/python3
"""module containing the class BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        initializes new instances
        args:
            args: won’t be used
            kwargs: dictionary with instance attributes and class type
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """default print message"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the instance into storage with updated time"""
        self.updated_at = datetime.now()
        storage.save()

    def remove(self):
        """removes object from storage
        key: "<class name>.<instance id>"
        """
        key = f"{self.__class__.__name__}.{self.id}"
        obj = storage.objects.pop(key, None)
        if obj:
            storage.save()

    def to_dict(self):
        """return a dictionary with the instance
        attributes while translating datetime type
        to string using ISO 8601 format"""
        output_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                output_dict.update({key: value.isoformat()})
            else:
                output_dict.update({key: value})
        output_dict.update({"__class__": self.__class__.__name__})
        output_dict.update({"__class__": self.__class__.__name__})
        return output_dict
