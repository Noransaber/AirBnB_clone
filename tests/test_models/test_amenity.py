#!/usr/bin/python3
"""
TEST
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """Init class to test"""
    def test_str(self):
    """Test the string """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_p(self):
    """If it's an instance of a classs"""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity))
