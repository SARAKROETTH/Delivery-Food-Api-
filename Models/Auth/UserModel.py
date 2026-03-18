from sqlalchemy import Column, Integer, String
from Config.DatabaseConfig import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    phoneNumber = Column(String(20), unique=True, index=True, nullable=False)
    imageUrl = Column(String(255), nullable=True)