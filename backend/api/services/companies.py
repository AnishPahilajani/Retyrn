from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from passlib.hash import bcrypt
from fastapi import HTTPException, Depends
from .users import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ALGORITHM, JWT_SECRET, jwt, oauth2_scheme

from database.models.company import Company
from .users import UserServices


class CompanyServices:       
    def create_company_service(self, db: Session, company: Company, email: str, user_id_FK: int):
        #user_FK = company_user_services.get_user_by_email_service(db=db, email=email)
        db_company = Company(
                    name = company.name,
                    address = company.address,
                    user_id = user_id_FK,
                    phone_number = company.phone_number
                    )
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company