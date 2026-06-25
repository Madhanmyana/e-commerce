from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas.user import UserCreate, UserLogin
from db.database import get_db
from models import user
from models.user import User
from core.security import hash_password,verify_password,create_jwt_token

def create_user(user_data:UserCreate,db:Session=Depends(get_db)):
    if db.query(User).filter(User.email==user_data.email).first():
        raise HTTPException(status_code=400,detail="email alredy exist")
    
    new_user=User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(user_data:OAuth2PasswordRequestForm,db:Session=Depends(get_db)):

    login_user=db.query(User).filter(User.email==user_data.username).first()

    if not login_user:
        raise HTTPException(status_code=400,detail="user not exist, register")
    
    if not verify_password(user_data.password,login_user.hashed_password):
        raise HTTPException(status_code=400,detail="invalid password")
    
    token=create_jwt_token({'sub':login_user.email})
    
    return {'access_token':token, 'token_type':'bearer'}