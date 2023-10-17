#!/usr/bin/python3
"""" Definition of FileStorage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ FileStorage class definition """
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in '__objects' the 'obj' with key '<obj class_name>.id' """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes '__objects' to into JSON file (path: '__file_path') """

        dict_objs = {
            key: (FileStorage.__objects[key]).to_dict()
            for key in FileStorage.__objects.keys()
        }

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(dict_objs, file)

    def reload(self):
        """ Deserializes a JSON file to '__objects'
        only if '__file_path' exists """
        try:
            path = FileStorage.__file_path
            with open(path, mode='r', encoding='utf-8') as file:
                loaded = json.load(file)
                for obj_dict in loaded.values():
                    cls = obj_dict['__class__']
                    obj_instance = eval(cls)(**obj_dict)
                    self.new(obj_instance)
        except FileNotFoundError:
            pass
