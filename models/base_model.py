#!/usr/bin/python3

from datetime import datetime
import uuid

class BaseModel:
    """
    Base class for other classes in the Air BnB project.

    Public instance attributes:
    - id: string - assign with a uuid when an instance is created.
    - created_at: datetime - assign with the current datetime when an instance is created.
    - updated_at: datetime - assign with the current datetime when an instance is created and updated every time you change your object.

    Public instance methods:
    - save(self): Updates the public instance attribute updated_at with the current datetime.
    - to_dict(self): Returns a dictionary containing all keys/values of __dict__ of the instance.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """
        Returns a string representation of the instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """

        self.updated_at = datetime.now()


    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Keys:
        - __class__: Class name of the object.
        - created_at: Creation timestamp in ISO format.
        - updated_at: Last update timestamp in ISO format.
        """

        return {
                '__class__': self.__class__.__name__,
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
                **self.__dict__
                }
