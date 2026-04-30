from pydantic import BaseModel, Field



class AdminCreate(BaseModel):
    username:str
    email:str
    password:str
    image_url:str = Field(..., max_length=72)


class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

