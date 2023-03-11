import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql import func

# from .user import User
from ..database_engine import Base
from .mixins import Timestamp
from sqlalchemy import UniqueConstraint


class Company(Timestamp, Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(), unique=True, index=True, nullable=False)
    address = Column(Text(), nullable=True)
    phone_number = Column(String(), index=True, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    # one to one relation with Company and user
    owner = relationship("User", back_populates="company_owner")
    
    #many to many relation with Users  table
    users = relationship("UserCompanyRelation", back_populates="company")
    
    
class UserCompanyRelation(Timestamp, Base):
    __tablename__ = "user_company"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, primary_key = True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False, primary_key=True)
    
    user = relationship("User", back_populates="companies")
    company = relationship("Company", back_populates="users")
    # __table_args__ = (
    #     UniqueConstraint('user_id', 'company_id', name='user_company_unique'),
    # )