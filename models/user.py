rom pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    file_url: str