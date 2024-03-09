#!/usr/bin/python3

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseMode
class TestBaseModelInstantiation(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = dt
        bmstr = base_model.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

class TestBaseModelToDict(unittest.TestCase):

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_to_dict_contains_correct_keys(self):
        base_model = BaseModel()
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("id", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

class TestBaseModelSave(unittest.TestCase):

    @classmethod
    def set_up_class(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_multiple_saves_update_order(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    @classmethod
    def tear_down_class(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

if __name__ == "__main__":
    unittest.main()
