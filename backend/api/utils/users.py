from sqlalchemy.orm import Session

from database.models.user import User
from pydantic_scheme.user import UserCreate


def get_user_utils(db: Session, user_id: int):
    print("CHECK")
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email_utils(db: Session, email: str):
    print("CHECK 1")
    return db.query(User).filter(User.email == email).first()


def get_users_utils(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user_utils(db: Session, user: UserCreate):
    hashed_password = user.password
    db_user = User(email=user.email, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user