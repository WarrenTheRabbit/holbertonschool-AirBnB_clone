#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    "Test case for Amenity class"

    def test_amenity_instance_creation(self):
        """Test that instance of Amenity is created correctly"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
