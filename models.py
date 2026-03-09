# Run this file only once python models.py
from sqlmodel import SQLModel, Field

class Teachers(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    Name: str
    age: int
    isactive: bool

class Admin(SQLModel, table = True):
    id: int = Field(default = None, primary_key = True)
    Name: str
    age: int
    isactive: bool
