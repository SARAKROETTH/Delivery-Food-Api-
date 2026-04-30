from pydantic import BaseModel


class AdminCreate(BaseModel):
    username :str
    phoneNumber :str
    codeCountry: str
    countryDialCode : str
    imageUrl :str
    role:str

class AdminRespone(BaseModel):
    username :str
    imageUrl :str
    

