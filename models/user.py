#!/usr/bin/python3
"""Module for User class"""
from base_model import BaseModel


class User(BaseModel):
    """Defines the User Type"""

    def __init__(self, first_name="", last_name="", email="", password=""):
        """Initializer for User instances

        Attr:
            first_name: str
            last_name: str
            email: str
            password: str
        """
        super().__init__()
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if password:
            self.password = password
