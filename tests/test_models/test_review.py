#!/usr/bin/python3
"""
TEST Review
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestBaseModel(unittest.TestCase):
"""Test Class"""
    def test_str(self):
        """Test for the string"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_p(self):
        """Check if its an instance of an onb"""
        review = Review()
        self.assertTrue(isinstance(review, Review))
