from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException, FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_scheme.user import UserCreate, User
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session

from api.services.users import UserServices
from database.database_engine import get_db, async_get_db
from sqlalchemy.ext.asyncio import AsyncSession
# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

user_services = UserServices()
router = fastapi.APIRouter() # initialize db session here
 
@router.get("/users", response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_services.get_users_service(db=db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    print("NOOO")
    db_user = user_services.get_user_service(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return user_services.create_user_service(db=db, user=user)

@router.put("/users/{user_id}", response_model=User, status_code=201)
def update_user(user_id: int, user: UserCreate ,db: Session = Depends(get_db)):
    db_user = user_services.get_user_service(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user_updated = user_services.update_user_service(db=db, db_user = db_user, user=user)        
    return db_user_updated

@router.get("/user/{email}", response_model=User) # idk why I should change path rom /users to /user if somone can explain it would be nice
def get_email(email: str, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/login/{email}", response_model=User)
def password_check(email: str, password: str, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.password == password:
        return db_user
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
@router.put("/user/{email}", response_model=User, status_code=201)
def update_user(email: str, user: UserCreate ,db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.email = email # Cant edit email with this PUT method
    db_user_updated = user_services.update_user_service(db=db, db_user = db_user, user=user)        
    return db_user_updated