#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all objects stored in the file.
        Returns:
            the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage
        Description:
            Sets in __objects the obj with key <obj class name>.id.
        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                deserialized_objects = json.load(file)
                for key, obj_dict in deserialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    self.__objects[key] = eval(class_name)(**obj_dict)
        except FileNotFoundError:
            pass
