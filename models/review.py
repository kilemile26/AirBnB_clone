#!/usr/bin/python3

"""
review class with public class attributes: place_id, user_id and text.
"""


from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class for storing information about reviews.
    """


    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize Review instance
        """
        super().__init__(*args, **kwargs)
        
        self.place_id = ""
        self.user_id = ""
        self.text = ""
