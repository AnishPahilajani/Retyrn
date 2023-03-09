from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException, FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes, HTTPBearer
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database.database_engine import get_db, async_get_db
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import bcrypt
import jwt
import re

from api.services.companies import CompanyServices, JWT_SECRET, oauth2_scheme, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES
from api.services.users import UserServices
from pydantic_scheme.companies import Company
from pydantic_scheme.user import User
# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

company_services = CompanyServices()
company_user_services = UserServices()

router = fastapi.APIRouter() # initialize db session here


"""
Allow users to create a Company
"""
@router.post("/{email}/company_new/", dependencies=[Depends(HTTPBearer())], status_code=201)
def create_company(company: Company, email: str ,db: Session = Depends(get_db)):
    db_user = company_user_services.get_user_by_email_service(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_company = company_services.create_company_service(db=db, company=company, email=email, user_id_FK=db_user.id )
    return db_company