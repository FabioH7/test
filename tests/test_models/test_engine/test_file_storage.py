#!/usr/bin/python3
"""Test Modules"""
import io
import sys
import unittest
import os
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    def test_storage(self):
        obj = FileStorage()
        self.assertEqual(type(obj.all()), dict)

    def test_filepath(self):
        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")

    def test_objects(self):
        obj = FileStorage()
        self.assertEqual(type(obj._FileStorage__objects), dict)
        self.assertEqual(obj._FileStorage__objects, obj.all())
    
    def test_methods(self):
        obj = FileStorage()
        base = BaseModel()
        result = obj.new(base)
        self.assertTrue(result is not None)
        result = obj.save()
        self.assertTrue(result is not None)
        result = obj.reload()
        self.assertTrue(result is not None)
