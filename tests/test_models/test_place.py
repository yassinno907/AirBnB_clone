#!/usr/bin/python3

from datetime import datetime
from models import place
from models.base_model import BaseModel
import unittest
import inspect

Place = place.Place
class TestPlaceDocs(unittest.TestCase):
    @classmethod
    def set_up_class(cls):
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_place_function_docstrings(self):
        for function in self.place_f:
            self.assertIsNot(function[1].__doc__, None,
                             "{:s} method needs a docstring".format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(function[0]))

    def test_place_module_docstring(self):
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")


class TestPlaceAttributes(unittest.TestCase):

    def test_name_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_is_subclass_of_base_model(self): 
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_max_guest_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_amenity_ids_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        p = Place()
        new_dict = p.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in p.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_dict = p.to_dict()
        self.assertEqual(new_dict["__class__"], "Place")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         p.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"],
                         p.updated_at.strftime(time_format))

    def test_latitude_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_attribute_exists(self):
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_str_representation(self):
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
if __name__ == "__main__":
    unittest.main()
