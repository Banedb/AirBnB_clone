#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_attributes(self):
        """Test if the attributes of User are present and initialized."""
        # Create an instance of User
        user = User()

        # Check if the attributes are present and initialized to default values
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """Test if User inherits from BaseModel."""
        # Create an instance of User
        user = User()

        # Check if User inherits from BaseModel
        self.assertIsInstance(user, BaseModel)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary."""
        # Create an instance of User
        user = User()

        # Get the dictionary representation of the instance
        user_dict = user.to_dict()

        # Check if the keys and values in the dictionary are correct
        self.assertEqual(user_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
