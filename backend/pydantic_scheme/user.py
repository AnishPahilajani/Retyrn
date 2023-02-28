from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    address: Optional[str] = None
    S3_link: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    S3_link: Optional[str] = None
    address: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True