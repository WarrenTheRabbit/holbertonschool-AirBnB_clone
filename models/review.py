#!/usr/bin/python3
"""Module for Review class"""
from base_model import BaseModel


class Review(BaseModel):
    """Defines the Review Type"""

    def __init__(self, place_id="", user_id="", text=""):
        """Initializer for Review instances

        Attr:
            place_id: str
            user_id: str
            text: str
        """
        super().__init__()
        if place_id:
            self.place_id = place_id
        if user_id:
            self.user_id = user_id
        if text:
            self.text = text
