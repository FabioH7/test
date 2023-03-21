#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls != None:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__:
                    obj_dict[key] = value
            return obj_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                content = f.read()
                if len(content) != 0:
                    obj = json.loads(content)
                    for key, value in obj.items():
                        value = eval(value['__class__'])(**value)
                        FileStorage.new(self, value)
        return True

    def delete(self, obj=None):
        """Method deletes given argument obj"""
        if obj != None:
            storage = self.all()
            for key, value in storage.items():
                if value == obj:
                    del storage[key]
                    break
