import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql import func


from ..database_engine import Base
from .mixins import Timestamp


# PREFERED Make your changes then run teh following 2 commands
# alembic downgrade base
# alembic upgrade head

# if you append to the database then re RUN
# alembic revision --autogenerate
# alembic upgrade head
# A new file will be created with the updated fields

# delete any revesion files under alembic/version DO NOT DO THIS Not all data will be regenerated
# re run alembic revision --autogenerate


class User(Timestamp, Base):
    __tablename__ = "users"
    # index is only used for improved performance, If you plan to retrive data using a certain column better have it
    id = Column(Integer, primary_key=True, index = True) 
    email = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(String(), index = True, nullable=True)
    last_name = Column(String(), index = True, nullable=True)
    password = Column(String(), index = True, nullable=True)
    phone_number = Column(String(), index = True, nullable=True)
    S3_link = Column(String(), nullable = True)
    address = Column(String(), nullable = True)
    
    # uselist = False => one to one relation
    truck_driver = relationship("TruckDriver", back_populates = "owner", uselist = False) # "owner" needs to be same name as TruckDriver table
    
    
    
class TruckDriver(Timestamp, Base):
    __tablename__ = "truck_drivers"
    id = Column(Integer, primary_key=True, index = True) 
    S3_link = Column(String(), nullable = True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    owner = relationship("User", back_populates="truck_driver") # access using user.profile.<whatever> # profile needs to be same name as in User table
    
    
    