from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    phoneNumber: str
    imageUrl: str | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    phoneNumber: str
    imageUrl: str | None = None
