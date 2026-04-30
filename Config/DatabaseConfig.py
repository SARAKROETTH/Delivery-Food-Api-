from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_HOST= os.getenv("DB_HOST")
DB_PORT= os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")



DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env")

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
