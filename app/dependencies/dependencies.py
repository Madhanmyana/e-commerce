from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException

from db.database import get_db
from core.security import verify_token
from models.user import User

oauth2_schema=OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):
    payload=verify_token(token)

    if not payload:
        raise HTTPException(status_code=401,detail='not authorized')
    
    user=db.query(User).filter(User.email==payload.get('sub')).first()

    if not user:
        raise HTTPException(status_code=401,detail='user not found')

    return user