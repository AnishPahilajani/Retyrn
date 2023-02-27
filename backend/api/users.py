from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException, FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_scheme.user import UserCreate, User
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session

from api.utils.users import get_users, get_user, get_user_by_email, create_user
from database.database_engine import get_db
#from api.crud.user import get_user, get_user_by_email, get_users, create_user

# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

router = fastapi.APIRouter()


        
        
@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users