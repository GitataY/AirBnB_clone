#!/usr/bin/python3
"""
module city
Defines city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines the city to look for"""
    state_id = ""
    name = ""
