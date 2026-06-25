import os
from dotenv import load_dotenv

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta

load_dotenv()

ALGORITHM=os.getenv("ALGORITHM")
SECRET_KEY=os.getenv("SECRET_KEY")

pwd_context=CryptContext(schemes="bcrypt")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_jwt_token(user_data:dict):
    payload=user_data.copy()
    payload.update({'exp':datetime.now(timezone.utc)+timedelta(minutes=30)})
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    
    except JWTError:
        return None