#!/usr/bin/python3

"""
Module: base_model
Defines the BaseModel class.
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    Base class for common attributes/methods of other classes
    in the Air BnB project.

    Public instance attributes:
    - id: string - assign with a uuid when an instance is created.
    - created_at: datetime - assign with the current datetime when an
    instance is created.
    - updated_at: datetime - assign with the current datetime when an
    instance is created and updated every time you change your object.

    Public instance methods:
    - save(self): Updates the public instance attribute updated_at with
    the current datetime.
    - to_dict(self): Returns a dictionary containing all keys/values
    of __dict__ of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #Call new(self) method on storage if it's a new instance
            from models import storage
            storage.new(self)


    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        #return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """

        self.updated_at = datetime.now()
        from models import storage
        storage.save()


    def to_dict(self):
        """
        Returns a dictionary representation containing all keys/values of __dict__ of the instance.

        Keys:
        - __class__: Class name of the object.
        - created_at: Creation timestamp in ISO format.
        - updated_at: Last update timestamp in ISO format.
        """

        return {
                '__class__': self.__class__.__name__,
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
                **self.__dict__
                }
