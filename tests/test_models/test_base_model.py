#!/usr/bin/python3
"""Test Modules"""
import io
import sys
import unittest
import os
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        base1 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_storage(self):
        base = BaseModel()
        self.assertNotEqual(len(storage.all()), 0)

    def test_save(self):
        base = BaseModel()
        time = base.save()
        self.assertEqual(base.updated_at, time)

    def test_to_dict(self):
        base = BaseModel()
        new_d = base.to_dict()
        self.assertEqual(new_d['id'], base.id)
        self.assertEqual(new_d['created_at'], base.created_at.isoformat())
        self.assertEqual(new_d['updated_at'], base.updated_at.isoformat())

    def test_to_str(self):
        base = BaseModel()
        x = base
        self.assertEqual(base, x)
