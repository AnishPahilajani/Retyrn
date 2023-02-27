from sqlalchemy.orm import Session

from database.models.user import User
from pydantic_scheme.user import UserCreate


def get_user_utils(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email_utils(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users_utils(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user_utils(db: Session, user: UserCreate):
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