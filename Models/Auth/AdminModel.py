from sqlalchemy import Column, String,Enum,DateTime,func
from Config.DatabaseConfig import Base
from sqlalchemy.dialects.postgresql import UUID

import uuid

class Admin(Base):
    __tablename__ = "admin"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(255),nullable=False )
    email = Column(String(100),unique=True ,nullable=True)
    password = Column(String(255),nullable=True)
    image_url = Column(String)

    #  create Date
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # update Date
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    ) 
