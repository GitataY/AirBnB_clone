#!/usr/bin/python3
"""
User module
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """It defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
