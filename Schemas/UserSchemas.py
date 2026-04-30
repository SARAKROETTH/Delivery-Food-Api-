from pydantic import BaseModel


class AdminCreate(BaseModel):
    username :str
    phoneNumber :str
    codeCountry: str
    countryDialCode : str
    image_url :str

class AdminRespone(BaseModel):
    username :str
    imageUrl :str
    

