from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException, FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes, HTTPBearer
from pydantic import BaseModel
from pydantic_scheme.user import UserCreate, User, UserAuth
from typing import Optional, List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import jwt
import re

from api.services.users import UserServices, JWT_SECRET, oauth2_scheme, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES
from database.database_engine import get_db, async_get_db
from sqlalchemy.ext.asyncio import AsyncSession
from  api.services.authentication import auth
from api.services.companies import CompanyServices, UserCompanyRelation
from pydantic_scheme.companies import Company
# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

user_services = UserServices()
user_company_services = CompanyServices()
router = fastapi.APIRouter() # initialize db session here

#CONSTANTS
EMAIL_REGEX = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
PASSWORD_REGEX = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[_#?!@$%^&*-]).{8,64}$"
NAME_REGEX = r'^[A-Za-z]{1,50}$'
@router.get("/users", dependencies=[Depends(auth.has_access)], response_model=List[User], tags = ['Users'])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_services.get_users_service(db=db, skip=skip, limit=limit)
    return users

'''
get user based on given user_id
'''
@router.get("/users/{user_id}", dependencies=[Depends(auth.has_access)], response_model=User, tags = ['Users'])
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_services.get_user_service(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


"""
Allow users to sign up using email and password

Email: email format
Password: at least 1 Upper, 1 Lower, 1 Number, 1 Special Character (_#?!@$%^&*-), min 8 chars, max 64 chars
Name: Letters and 1-50 characters
Examples: 
    Email: hello@gmail.com
    Password: Test12345!
    First Name: Hello
    Last Name: World
"""
@router.post("/signup", status_code=201, tags = ['Users'])
def create_user(user: UserCreate, db: Session = Depends(get_db),):
    db_user = user_services.get_user_by_email_service(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    elif not re.match(EMAIL_REGEX, user.email):
        raise HTTPException(status_code=401, detail="Invalid Email Format")
    elif not re.match(PASSWORD_REGEX, user.password):
        raise HTTPException(status_code=401, detail="Invalid Password Format")
    elif not re.match(NAME_REGEX, user.first_name):
        raise HTTPException(status_code=401, detail="Invalid First Name")
    elif not re.match(NAME_REGEX, user.last_name):
        raise HTTPException(status_code=401, detail="Invalid Last Name")
    db_user = user_services.create_user_service(db=db, user=user)
    access_token_expires = timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_services.create_access_token_service(data={"email": db_user.email,"user_id":db_user.id}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'toke_type' : 'bearer'}

'''
update user data based on user_id, email can be changed
'''
@router.put("/users/{user_id}", dependencies=[Depends(auth.has_access)], response_model=User, status_code=201, tags = ['Users'])
def update_user(user_id: int, user: UserCreate ,db: Session = Depends(get_db)):
    db_user = user_services.get_user_service(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user_updated = user_services.update_user_service_put(db=db, db_user = db_user, user=user)        
    return db_user_updated

'''
get user based on given email
'''
@router.get("/user/{email}", dependencies=[Depends(auth.has_access)], response_model=User, tags = ['Users']) # idk why I should change path rom /users to /user if somone can explain it would be nice
def get_email(email: str, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# @router.get("/login/{email}", response_model=User)
# def password_check(email: str, password: str, db: Session = Depends(get_db)):
#     db_user = user_services.get_user_by_email_service(db=db, email=email)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     if db_user.password == password:
#         return db_user
#     else:
#         raise HTTPException(
#             status_code=401,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

'''
update user data based on user_id, email can NOT be changed
'''   
@router.patch("/user/{email}", dependencies=[Depends(auth.has_access)], response_model=User, status_code=201, tags = ['Users'])
def update_user(email: str, user: dict ,db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user_updated = user_services.update_user_service_patch(db=db, db_user = db_user, user=user)        
    
    # for k, v in user.items(): IDK why this does not work and forces me to do a brute force way
    #         print(k, v)
    #         if k in db_user.__dict__.keys():
    #             print(f"k: {k}, typ: {type(k)}: {db_user.__dict__[k]}")
    #             db_user.__dict__[k] = v
    #             print(f"k: {k}, typ: {type(k)}: {db_user.__dict__[k]}")    
    db.commit()
    db.refresh(db_user_updated)
    return db_user_updated

@router.post("/token", tags = ['Users'])
async def password_check(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=form_data.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if bcrypt.verify(form_data.password, db_user.password):       
        # access_token = jwt.encode(dict(db_user_dict), JWT_SECRET, algorithm = JWT_ALGORITHM)
        access_token_expires = timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = user_services.create_access_token_service(
            data={"email": db_user.email, "user_id":db_user.id}, expires_delta=access_token_expires
        )
        return {'access_token': access_token, 'toke_type' : 'bearer'}
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
@router.post("/token/no-oauth", tags = ['Users'])
async def password_check(form_data: UserAuth, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email_service(db=db, email=form_data.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Invalid Username or Password")
    if bcrypt.verify(form_data.password, db_user.password):       
        # access_token = jwt.encode(dict(db_user_dict), JWT_SECRET, algorithm = JWT_ALGORITHM)
        access_token_expires = timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = user_services.create_access_token_service(
            data={"email": db_user.email,"user_id":db_user.id}, expires_delta=access_token_expires
        )
        return {'access_token': access_token, 'toke_type' : 'bearer'}
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get('/you', response_model=User, tags = ['Users'])
def get_user_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = user_services.get_current_user_service(db, token)
    return user    

"""
API that defines which company users work for
"""
@router.post("/signup-company", status_code=201, tags = ['Users'])
def add_company(company_name: str, token = Depends(auth.has_access),db: Session = Depends(get_db)):
    db_company = user_company_services.get_company_by_name_service(db=db, name=company_name)
    if db_company == None:
        raise HTTPException(status_code=404, detail="Company does not exists")
    user_company = user_services.add_company_service_post(db=db, user_id=token['user_id'], company_id=db_company.id)
    return user_company