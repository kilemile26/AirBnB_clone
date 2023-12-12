#!/usr/bin/python3
"""
City class for storing information about cities.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class with public class attributes: state_id, name
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize City instance
        """

        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
