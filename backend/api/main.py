from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# termianl command to run this code
# uvicorn main:app --reload 

# do all installations with pipenv install <package name>


app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

fakedb = [] # we will use SQL here

class userData(BaseModel):
    id: int
    FirstName: str
    LastName: str
    hasInsurance: bool
    InsuranceWorth: float
    address: Optional[str] = None
        

@app.get("/")
def read_root():
    return {"greetings": "welcome"}

@app.get("/users")
def get_users():
    return fakedb


# take parametrs from URL
@app.get("/users/{user_id}")
def get_user(user_id: int):
    userid = user_id-1
    return fakedb[userid]


@app.post("/users")
def add_user(user: userData):
    fakedb.append(user.dict())
    return fakedb[-1] 

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    fakedb.pop(user_id-1)
    return {"task": "deletion"}


