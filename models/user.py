# models/user.py
"""
user management class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel with public attributes: email, password, first_name, last_name.
    All attributes are initialized to empty strings.
    """
    super().__init__(*args, **kwargs)
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
