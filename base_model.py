#!/usr/bin/python3
"""
   BaseModel is the parent of all the future
   that contain common attributes
"""
from datetime import datetime, date
import uuid
from models import storage


class BaseModel():
    """
       Definition of the behavior of Base Model
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of the differents attributes of base model:

        Args:
             *args: Receive the arguments in list
             **kwargs: Receive the argumenst in form of keyword
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Description of the class [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """
           Update the public instance update_at
           with the current_time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
           Returns:
                 Dictionary with key and values of instance
        """
        d = {}

        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = d["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        d["updated_at"] = d["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        return d
