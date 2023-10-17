#!/usr/bin/python3
""""
This module defines BaseModel class
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ Init method for BaseModel """
        time_f = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_f)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Returns the string represetation of a BaseModel instance """
        return (
                "[{}] ({}) {}"
                .format(self.__class__.__name__,
                        self.id,
                        self.__dict__
                        )
                )

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)
