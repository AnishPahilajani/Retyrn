from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from passlib.hash import bcrypt
from fastapi import HTTPException, Depends
from .users import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ALGORITHM, JWT_SECRET, jwt, oauth2_scheme

from database.models.company import Company
from .users import UserServices


class CompanyServices:       
    def create_company_service(self, db: Session, company: Company, email: str, user_id_FK: int):
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
    
    def get_companies_service(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Company).offset(skip).limit(limit).all()
    
    def get_companies_under_a_user_service(self, db: Session, user_id_FK: int):
        return db.query(Company).filter(Company.user_id == user_id_FK).all()
    
    def get_company_by_name_service(self, db: Session, name: str):
        return db.query(Company).filter(Company.name == name).first()
    
    def update_company_service_patch(self, db: Session, db_company, company: dict):
        for k, v in company.items():
            if k == "address":
                db_company.address = v
                db_company.updated_at = datetime.utcnow()
            elif k == "phone_number":
                db_company.phone_number = v
                db_company.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_company)
        return db_company