import fastapi
from fastapi import FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

router = fastapi.APIRouter()

fakedb = [] # we will use SQL here

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    password: str
    email: str
    phone_number: str
    S3_link: Optional[str] = None
    address: Optional[str] = None
    
    class Config:
        orm_mode = True
        

@router.get("/")
def read_root(q: str = Query(None)):
    return {"greetings": q}

@router.get("/users", response_model=List[User])
def get_users():
    return fakedb


# take parametrs from URL
@router.get("/users/{user_id}")
def get_user(user_id: int):
    userid = user_id-1
    return fakedb[userid]


@router.post("/users")
def add_user(user: User):
    fakedb.append(user.dict())
    return fakedb[-1] 

@router.delete("/users/{user_id}")
def delete_user(user_id: int = Path(..., description="The ID of the user you want to delete", ge=0)): # >= 0
    fakedb.pop(user_id-1)
    return {"task": "deletion"}


