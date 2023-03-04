from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from database.models.user import User
from pydantic_scheme.user import UserCreate
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from passlib.hash import bcrypt
import jwt
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
JWT_SECRET = '0850fa46da3812d64eaaaa47009db86b2b6105c1d996350cc12b0ce45edfcf08'
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
        hashed_password = bcrypt.hash(user.password) # hash here
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
        hashed_password = bcrypt.hash(user.password) # hash here
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
    
    def create_access_token_service(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
        
    def get_current_user_service(self, db: Session, token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user = self.get_user_by_email_service(db=db, email=payload.get('email'))#User.get(id=payload.get('email'))
        except:
            raise HTTPException(
                status_code=401, 
                detail='Invalid username or password'
            )
        return user