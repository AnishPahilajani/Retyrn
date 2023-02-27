from pydantic import BaseModel
from datetime import datetime
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str
    phone_number: str
    address: str
    S3_link: str
    created_at: datetime
    updated_at: datetime


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    S3_link: str
    address: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True