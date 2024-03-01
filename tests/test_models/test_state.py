#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test case for State class"""

    def test_that_state_instance_creation(self):
        state = State()
        self.assertEqual(state.name, "")
