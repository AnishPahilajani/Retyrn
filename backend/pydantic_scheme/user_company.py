from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCompanyRelation(BaseModel):
    user_id: int
    company_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True
    