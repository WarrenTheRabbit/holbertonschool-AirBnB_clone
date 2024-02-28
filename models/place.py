#!/usr/bin/python3
"""Module for Place class"""
from base_model import BaseModel


class Place(BaseModel):
    """Defines the Place Type"""

    def __init__(self, name="", city_id="", user_id="",
                 description="", number_rooms=0, number_bathrooms=0,
                 max_guest=0, price_by_night=0, latitude=0.0,
                 longitude=0.0, amenity_ids=[]
                 ):
        """Initializer for Place instances
        Attr:
            city_id: str
            user_id: str
            name: str
            description: str
            number_rooms: int
            number_bathrooms: int
            max_guest: int
            price_by_night: int
            latitude: float
            longitude: float
            amenity_ids: [str]
        """

        super().__init__()
        if name:
            self.name = name
        if city_id:
            self.city_id = city_id
        if user_id:
            self.user_id = user_id
        if description:
            self.description = description
        if number_rooms:
            self.number_rooms = number_rooms
        if number_bathrooms:
            self.number_bathrooms = number_bathrooms
        if max_guest:
            self.max_guest = max_guest
        if price_by_night:
            self.price_by_night = price_by_night
        if longitude:
            self.longitude = longitude
        if latitude:
            self.latitude = latitude
        self.amenity_ids = amenity_ids
