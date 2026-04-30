from sqlalchemy import Column, String,Enum,DateTime, func
from Config.DatabaseConfig import Base
from sqlalchemy.dialects.postgresql import UUID

import enum ,uuid


class UserRole(str, enum.Enum):
    user = "user"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, index=True, nullable=False)
    phoneNumber = Column(String(20), unique=True, index=True, nullable=False)
    codeCountry = Column(String(2), nullable=False)
    countryDialCode = Column(String(6), nullable=False)
    imageUrl = Column(String(255), nullable=True)
    role = Column(Enum(UserRole, name="user_role"), default=UserRole.user)

    #  create Date
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # update Date
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    ) 

