from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class CreateCompany(BaseModel):
    name: str
    address: str
    phone_number: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Company(BaseModel):
    id: int
    name: str
    address: str
    user_id: int
    phone_number: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True