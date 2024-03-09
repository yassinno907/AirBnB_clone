#!/usr/bin/python3

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import unittest

STATE = state.State

class TestStateDocs(unittest.TestCase):
    @classmethod
    def set_up_class(cls):
        cls.state_functions = inspect.getmembers(STATE, inspect.isfunction)

    def test_module_docstring(self):
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(STATE.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(STATE.__doc__) >= 1,
                        "State class needs a docstring")

    def test_method_docstrings(self):
        for func_name, func in self.state_functions:
            self.assertIsNot(func.__doc__, None,
                             "{:s} method needs a docstring".format(func_name))
            self.assertTrue(len(func.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func_name))


class TestStateFunctionality(unittest.TestCase):

    def test_subclass_of_BaseModel(self):
        state_instance = STATE()
        self.assertIsInstance(state_instance, BaseModel)
        self.assertTrue(hasattr(state_instance, "id"))
        self.assertTrue(hasattr(state_instance, "created_at"))
        self.assertTrue(hasattr(state_instance, "updated_at"))

    def test_name_attribute(self):
        state_instance = STATE()
        self.assertTrue(hasattr(state_instance, "name"))
        self.assertEqual(state_instance.name, "")

    def test_to_dict_creates_dictionary(self):
        s = STATE()
        new_dict = s.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in s.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = STATE()
        new_dict = s.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         s.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"],
                         s.updated_at.strftime(time_format))

    def test_string_representation(self):
        state_instance = STATE()
        expected_string = "[State] ({}) {}".format(
            state_instance.id, state_instance.__dict__)
        self.assertEqual(expected_string, str(state_instance))

if __name__ == "__main__":
    unittest.main()
