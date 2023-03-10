import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql import func

# from .user import User
from ..database_engine import Base
from .mixins import Timestamp


class Company(Timestamp, Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(), unique=True, index=True, nullable=False)
    address = Column(Text(), nullable=True)
    phone_number = Column(String(), index=True, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    owner = relationship("User", back_populates="company_owner")