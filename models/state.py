#!/usr/bin/python3
"""
State class for storing information about states.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class with public class attribute: name.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize State instance
        """

        supre().__init__(*args, **kwargs)
        self.name = ""
