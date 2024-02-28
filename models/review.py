#!/usr/bin/python3
"""Module for Review class"""
from base_model import BaseModel


class Review(BaseModel):
    """Defines the Review Type"""
    place_id = ""
    user_id = ""
    text = ""
