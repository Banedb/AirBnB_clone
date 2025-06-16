#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_attributes(self):
        """Test if the attributes of Review are present and initialized."""
        # Create an instance of Review
        review = Review()

        # Check if the attributes are present and initialized to default values
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        # Create an instance of Review
        review = Review()

        # Check if Review inherits from BaseModel
        self.assertIsInstance(review, BaseModel)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary."""
        # Create an instance of Review
        review = Review()

        # Get the dictionary representation of the instance
        review_dict = review.to_dict()

        # Check if the keys and values in the dictionary are correct
        self.assertEqual(review_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
