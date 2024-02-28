#!/usr/bin/python3
"""Module for State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines the State Type"""

    def __init__(self, name=""):
        """Initializer for State instances

        Attr:
            name: str
        """
        super().__init__()
        if name:
            self.name = name
