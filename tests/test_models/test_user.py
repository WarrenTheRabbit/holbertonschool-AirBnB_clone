#!/usr/bin/python3
"""Module contains unit tests for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test case for User class"""

    def test_user_instance_instantiation(self):
        """Tests that a User instance is instantiated
        with all attributes available
        """
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.last_name, "")
