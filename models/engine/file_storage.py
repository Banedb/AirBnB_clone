#!/usr/bin/python3
"""file_storage module"""

from datetime import datetime
import json
import os


class FileStorage:
    """Serialises and deserialises instances to and from a json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all instances"""
        # print(f"This is objects: {self.__objects}")
        return self.__objects

    def delete(self, key):
        """Deletes an instance."""
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def new(self, obj):
        """Stores new instance in private class attribute `__objects`"""
        name = obj.__class__.__name__ + "." + obj.id
        self.__objects[name] = obj

    def save(self):
        """Serialises instances in `__objects` to json file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            new_dict = {nameid: obj.to_dict()
                        for nameid, obj in self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserialises instances from json file to `__objects`"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                from console import classes
                dict_str = json.load(f)
                for key, val in dict_str.items():
                    cls = classes.get(key.split(".")[0])
                    if cls:
                        self.__objects[key] = cls(**val)
