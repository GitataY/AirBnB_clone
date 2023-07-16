#!/usr/bin/python3
"""
review module
Defines the review class made by users about a place
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""
