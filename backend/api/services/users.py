from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from database.models.user import User
from pydantic_scheme.user import UserCreate




class UserServices:       
    def get_user_service(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    # async def get_user_utils(db: AsyncSession, user_id: int):
    #     query = select(User).where(User.id == user_id)
    #     result = await db.execute(query)
    #     return result.scalar_one_or_none()


    def get_user_by_email_service(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()


    def get_users_service(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()


    def create_user_service(self, db: Session, user: UserCreate):
        hashed_password = user.password
        db_user = User(email=user.email, 
                    password = hashed_password,
                    first_name = user.first_name,
                    last_name = user.last_name,
                    phone_number = user.phone_number,
                    S3_link = user.S3_link,
                    address = user.address
                    )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user_service(self, db: Session, db_user, user: UserCreate):
        hashed_password = user.password
        if (db_user.email != user.email) and self.get_user_by_email_service(db=db, email =user.email):
            raise HTTPException(status_code=400, detail="Email is already registered")
        db_user.email = user.email
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.password = hashed_password
        db_user.phone_number = user.phone_number
        db_user.S3_link = user.S3_link
        db_user.address = user.address
        db_user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_user)
        return db_user