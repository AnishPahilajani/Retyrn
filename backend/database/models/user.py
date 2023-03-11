import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql import func

from .company import Company
from ..database_engine import Base
from .mixins import Timestamp


# PREFERED Make your changes in alambic/versions/ then run teh following 2 commands
# WARNING: DB is deleted
# alembic downgrade base
# make changes
# alembic upgrade head

# if make changes to THIS file
# make changes to this file
# alembic revision --autogenerate
# alembic upgrade head
# A new file will be created with the updated fields

# delete any revesion files under alembic/version DO NOT DO THIS Not all data will be regenerated
# alembic downgrade base
# re run alembic revision --autogenerate

class User(Timestamp, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True) 
    email = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(String(), index=True, nullable=True)
    last_name = Column(String(), index=True, nullable=True)
    password = Column(String(), index=True, nullable=True)
    phone_number = Column(String(), index=True, nullable=True)
    S3_link = Column(String(), nullable=True)
    address = Column(Text(), nullable=True)
    
    # uselist = False => one to one relation
    truck_driver = relationship("TruckDriver", back_populates="truck_owner", uselist=False) # "owner" needs to be same name as TruckDriver table
    company_owner = relationship("Company", back_populates="owner", uselist=False)
    
    #many to many realtion between User and Company
    companies = relationship("UserCompanyRelation", back_populates="user")
    
    
class TruckDriver(Timestamp, Base):
    __tablename__ = "truck_drivers"
    id = Column(Integer, primary_key=True, index = True) 
    S3_link = Column(String(), nullable = True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    truck_owner = relationship("User", back_populates="truck_driver") # access using user.profile.<whatever> # profile needs to be same name as in User table
    
    
    