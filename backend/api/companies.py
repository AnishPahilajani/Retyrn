from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException, FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes, HTTPBearer
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
from pydantic_scheme.companies import Company, CreateCompany
from pydantic_scheme.user import User
from  api.services.authentication import auth
# termianl command to run this code
# uvicorn users:app --reload 

# do all installations with pipenv install <package name>

company_services = CompanyServices()
company_user_services = UserServices()

router = fastapi.APIRouter() # initialize db session here


'''
Allow users to create a Company.
token is dictionary with following data:
{
  "email": "anish@anish.com",
  "user_id": 3,
  "exp": 1678393118
}
If this token exists, a company is created under this user.
'''
@router.post("/company_new", dependencies=[Depends(auth.has_access)], status_code=201, tags = ['Company'])
def create_company(company: CreateCompany,token = Depends(auth.has_access) ,db: Session = Depends(get_db)):
  db_company = company_services.get_company_by_name_service(db=db, name=company.name)
  if db_company:
    raise HTTPException(status_code=400, detail="Company is already registered")
  if company_services.get_company_by_owner_service(db=db, user_id=token['user_id']):
    raise HTTPException(status_code=400, detail="You cant have more than one owner for 1 company")
  db_company = company_services.create_company_service(db=db, company=company, email=token['email'], user_id_FK=token['user_id'] )
  return db_company
  
'''
get all companies
'''
@router.get("/companies", dependencies=[Depends(auth.has_access)], response_model=List[Company], tags = ['Company'])
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = company_services.get_companies_service(db=db, skip=skip, limit=limit)
    return companies
  
'''
get company of user logged in
'''
@router.get("/companies-user", dependencies=[Depends(auth.has_access)], response_model=List[Company], tags = ['Company'])
def get_companies_under_user(token = Depends(auth.has_access), db: Session = Depends(get_db)):
    companies = company_services.get_companies_under_a_user_service(db=db, user_id_FK=token['user_id'])
    return companies
  
'''
update company details
'''
@router.patch("/company/{name}", dependencies=[Depends(auth.has_access)], response_model=Company, status_code=201, tags = ['Company'])
def update_company(name: str, company: dict ,token = Depends(auth.has_access), db: Session = Depends(get_db)):
    db_company = company_services.get_company_by_name_service(db=db, name=name)
    if db_company is None:
      raise HTTPException(status_code=404, detail="User not found")
    if db_company.user_id != token['user_id']:
      raise HTTPException(status_code=403, detail="User is not owner of this company!")
    db_company_updated = company_services.update_company_service_patch(db=db, db_company=db_company, company=company)   
    if db_company_updated is None:
      raise HTTPException(status_code=422, detail="Cant change name of company")
    db.commit()
    db.refresh(db_company_updated)
    return db_company_updated 
  
'''
Get all employees under a company
'''
@router.get("/company/{name}", dependencies=[Depends(auth.has_access)], response_model=List[User], status_code=200, tags = ['Company'])
def get_employees(company_name: str, token = Depends(auth.has_access), db: Session = Depends(get_db)):
  employee_ids = company_services.get_employees_of_company(db=db, name=company_name)
  users = []
  for employee_id in employee_ids:
    user = company_user_services.get_user_service(db=db, user_id=employee_id.user_id)
    users.append(user)
  return(users)