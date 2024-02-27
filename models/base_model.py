#!/usr/bin/python3
"""module containing the class BaseModel"""
import uuid
import datetime


class BaseModel():
    """class BaseModel"""
    def __init__(self):
        """
        initializes new instances
        args:
            id: uses uuid4 to create a unique id
            created_at: use datetime to store current time
            updated_at: use datetime to store current time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """default print message"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the attribute updated_at with current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """return a dictionary with the instance
        attributes while translating datetime type
        to string using ISO 8601 format"""
        output_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                output_dict.update({key: value.isoformat()})
            else:
                output_dict.update({key: value})
        return output_dict
