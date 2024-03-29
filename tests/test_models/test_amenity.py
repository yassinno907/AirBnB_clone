#!/usr/bin/python3

import inspect
from models import amenity
from models.base_model import BaseModel
import unittest
from datetime import datetime

AMENITY = amenity.Amenity


class TestAmenityAttributes(unittest.TestCase):

    def test_name_attribute_exists(self):
        amenity = AMENITY()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dictionary(self):
        am = AMENITY()
        new_dict = am.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in am.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_attribute_values(self):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = AMENITY()
        new_dict = am.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         am.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"],
                         am.updated_at.strftime(time_format))

    def test_is_subclass_of_base_model(self):
        amenity = AMENITY()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_string_representation(self):
        amenity = AMENITY()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))


class TestAmenityInstantiation(unittest.TestCase):

    @classmethod
    def set_up(cls):
        cls.amenity_f = inspect.getmembers(AMENITY, inspect.isfunction)

    def test_amenity_class_docstring(self):
        self.assertIsNot(AMENITY.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(AMENITY.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_function_docstrings(self):
        for function in self.amenity_f:
            self.assertIsNot(function[1].__doc__, None,
                             "{:s} method needs a docstring".format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(function[0]))

    def test_amenity_module_docstring(self):
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")
if __name__ == "__main__":
    unittest.main()
