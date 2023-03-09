from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

# GRANT ALL ON SCHEMA public TO anish;
# grant usage on schema public to anis;
# grant all priviliges on database retyrn_db to anish
DATABASE_URL = "sqlite:///./sql_app.db"#'postgresql://postgres:postgres@localhost:5432/retyrn_db'
ASYNC_DATABASE_URL = 'postgresql+asyncpg://anish:anish@localhost:5432/retyrn_db'


async_engine = create_async_engine(ASYNC_DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={}, future = True)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine, future = True)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()
    
# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()