#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        objects_dict = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = value["__class__"]
                    self.__objects[key] = eval(class_name + "(**value)")
        except FileNotFoundError:
            pass
