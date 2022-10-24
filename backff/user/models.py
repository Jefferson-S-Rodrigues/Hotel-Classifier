from datetime import datetime
from typing import Union
import uuid

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    _id: uuid = uuid.uuid4()
    username: str
    email: Union[str, None] = None
    password: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: bool = False
    create_at: datetime = datetime.now()


class UserInDB(User):
    password: str


class HotelRequest(BaseModel):
    _id: uuid = uuid.uuid4()
    username: Union[str, None] = None
    name: str
    index_name: str
    n: int
    filter_name: Union[str, None] = None
