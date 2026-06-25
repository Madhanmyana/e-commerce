from pydantic import BaseModel,EmailStr
from datetime import datetime

# request schema
class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str


# response schema
class UserResponse(BaseModel):
    id:int
    username:str
    email:EmailStr
    role:str
    created_at:datetime

class LoginResponse(BaseModel):
    access_token:str
    token_type:str