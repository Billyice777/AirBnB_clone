#!/usr/bin/python3
""" Class user """

from models.base_model import BaseModel


class User(BaseModel):
    """ Public features of the User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
