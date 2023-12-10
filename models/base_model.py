"""
parent class of the Air BnB project
"""
from datetime import datetime
import uuid

class BaseModel:
    """
    initialization of the project's attributes
    """
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """
    method to set the output format
    """
    def __Str__(self):
        return f"[<class name>] (<self.id>) <self.__dict__>"

    """
    updates the public instance attribute updated_at with the current datetime
    """
    def save(self):
        self.updated_at = datetime.now()

    """
    returns a dictionary containing all keys/values of __dict__ of the instance
    """
    def to_dict(self):
        return self.__dict__
        self.__class__
        created_at = created_at.isoformat()
        updated_at = updated_at.isoformat()
