#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    "Test case for City class"

    def test_city_instance_creation(self):
        """Test that instance of City is created correctly"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
