#!/usr/bin/python3
"""Unit tests for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    "Test case for Place class"

    def test_place_instance_creation(self):
        """Test that instance of Place is created correctly"""
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
