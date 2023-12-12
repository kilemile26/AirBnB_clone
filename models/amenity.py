#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class for storing information about amenities.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize Amenity instance
        """

        super().__init__(*args, **kwargs)
        self.name = ""
