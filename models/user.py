#!/usr/bin/python3
"""
define user class's module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user instance
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

