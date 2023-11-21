from typing import Optional, Union
from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    username: str
    password: str


class User(BaseModel):
    fullname: Optional[str] = Field(None)
    username: str
    location: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    age: Optional[int] = Field(None)
    password: str
