#!/usr/bin/python3
"""Test Modules"""
import io
import sys
import unittest
import os
import datetime
from models.amenity import Amenity
from models import storage


class TestUser(unittest.TestCase):

    def test_attributes(self):
        base1 = Amenity()
        base2 = Amenity()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        base1 = Amenity()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_all_attributes(self):
        base = Amenity()
        self.assertEqual(base.name, '')
