#!/usr/bin/python3
"""Module for Amenity class"""
from base_model import BaseModel


class Amenity(BaseModel):
    """Defines the Amenity Type"""

    def __init__(self, name=""):
        """Initializer for Amenity instances
        Attr:
            name: str
        """
        super().__init__()
        if name:
            self.name = name
