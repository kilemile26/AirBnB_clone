#!/usr/bin/python3
"""
user management class
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class with public attributes: email, password, first_name, last_name.
    All attributes are initialized to empty strings.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize User instance
        """

        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
