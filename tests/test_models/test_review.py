#!/usr/bin/python3
"""Unit tests for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for Review class"""

    def test_review_instance_creation(self):
        """Test that review instance is created"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
