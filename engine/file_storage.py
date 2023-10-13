#!/usr/bin/python3

import json


class FileStorage:
        """ Definition of FileStorage class """
        __file_path = "file.json"
        __objects = {}

        def all(self):
            """
               Returns:
                     the dictionary __objects
            """
            return self.__objects

        def new(self, obj):
            """ Sets in __objects the obj with key <obj class name>.id """
            key = str(obj.__class__.__name__ + "." + obj.id)
            self.__objects[key] = obj.to_dict()

        def save(self):
            """ Serializes __objects to the JSON file """
            with open(self.__file_path, "w") as f:
                f.write(json.dumps(self.__objects))

        def reload(self):
            """ Deserializes the JSON file to __objects if it exists """
            try:
                with open(self.__file_path, "r") as f:
                    d = f.read()
                self.__objects = json.loads(d)
            except:
                pass
