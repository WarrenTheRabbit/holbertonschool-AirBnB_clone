#!/usr/bin/python3
"""Module for City class"""
from base_model import BaseModel


class City(BaseModel):
    """Defines the City Type"""

    def __init__(self, name="", state_id=""):
        """Initializer for City instances

        Attr:
            name: str
            state: str
        """
        super().__init__()
        if name:
            self.name = name
        if state_id:
            self.state_id = state_id
