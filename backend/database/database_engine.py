from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

sql_settings = {"qguser":"anish", "pgpassword":"anish", "pghost":"localhost", "pgport":5432, "pgdb":"retyrn_db"}
# GRANT ALL ON SCHEMA public TO anish;
# grant usage on schema public to anis;
# grant all priviliges on database retyrn_db to anish
DATABASE_URL = 'postgresql+psycopg2://anish:anish@localhost:5432/retyrn_db'#'postgresql://postgres:postgres@localhost:5432/retyrn_db'

engine = create_engine(DATABASE_URL, connect_args={}, future = True)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine, future = True)

Base = declarative_base()
    
# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()