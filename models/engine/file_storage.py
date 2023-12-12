#!/usr/bin/python3
"""
Module: file_storage
Defines the FileStorage class.
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class for serializing/deserializing instances to/from JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
