#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from unittest.mock import patch
from io import StringIO
import json
import os


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel class."""

    def setUp(self):
        """Sets up test cases."""
        self.tearDown()
        storage._FileStorage__objects = {}
        # Check if the id attribute is not None

    def tearDown(self):
        """Resets FileStorage data."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_instanstiation(self):
        """Tests instance creation and errors"""
        # Create an instance of BaseModel
        base_model = BaseModel()
        self.assertEqual(str(type(base_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base_model, BaseModel)
        # Check if the id attribute is not None
        self.assertIsNotNone(base_model.id)

        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_datetime(self):
        """Tests datetime."""
        base_model = BaseModel()
        date_now = datetime.now()
        diff = base_model.updated_at - base_model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = base_model.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_str_method(self):
        """Test for expected string output."""

        # Create an instance of BaseModel
        base_model = BaseModel()
        # Check if __str__ method returns the expected string representation
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        """Tests save method."""
        base_model = BaseModel()
        with patch('models.base_model.storage') as mock_storage:
            base_model.save()
            self.assertTrue(mock_storage.save.called)

        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        d = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(storage._FileStorage__file_path))
        with open(storage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

        # no args
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        # excess args
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, "dyi7")
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict_method(self):
        """Test for expected dictionary output."""

        # Create an instance of BaseModel
        base_model = BaseModel()
        # Get the dictionary representation of the instance
        model_dict = base_model.to_dict()
        # Check if the keys and values in the dictionary are correct
        self.assertEqual(model_dict['__class__'],
                         'BaseModel')
        self.assertEqual(model_dict['id'],
                         base_model.id)
        self.assertEqual(model_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         base_model.updated_at.isoformat())

        # no argument
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        # excess arguments
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, "fyikkg")
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
