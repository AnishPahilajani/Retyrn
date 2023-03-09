from fastapi import FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

# termianl command to run this code
# uvicorn main:app --reload 

# do all installations with pipenv install <package name>

from api import users, companies
from database.database_engine import engine
from database.models import user

user.Base.metadata.create_all(bind = engine)


app = FastAPI(
    title = "Retyrn API"
)
 
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


app.include_router(users.router)
app.include_router(companies.router)