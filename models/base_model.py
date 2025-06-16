#!/usr/bin/python3
"""base_model module"""

from models import storage
from datetime import datetime
import uuid


class BaseModel:
    """Defines the base class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """User-friendly print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def delete(self):
        """Deletes an instance."""
        key = self.__class__.__name__ + "." + self.id
        storage.delete(key)

    def save(self):
        """Updates instances and saves to json file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts object attributes to dict"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()

        return new_dict
