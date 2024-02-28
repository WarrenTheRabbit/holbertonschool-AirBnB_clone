#!/usr/bin/python3
"""Module for User class"""
from base_model import BaseModel


class User(BaseModel):
    """Defines the User Type"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
