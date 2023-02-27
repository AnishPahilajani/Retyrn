from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException, FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_scheme.user import UserCreate, User
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session

from api.utils.users import get_users_utils, get_user_utils, get_user_by_email_utils, create_user_utils
from database.database_engine import get_db

# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

router = fastapi.APIRouter()


        
        
@router.get("/users", response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users_utils(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_utils(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users", response_model=User, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email_utils(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user_utils(db=db, user=user)