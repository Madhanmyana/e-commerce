from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from services.user_service import create_user,login
from schemas.user import UserResponse, UserCreate, LoginResponse, UserLogin
from db.database import get_db
from dependencies.dependencies import get_current_user

router=APIRouter()


@router.post('/register',response_model=UserResponse)
def register_user(user_data:UserCreate,db:Session=Depends(get_db)):
    return create_user(user_data,db)

@router.post('/login',response_model=LoginResponse)
def login_user(user_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return login(user_data,db)

@router.get('/me',response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):
    return current_user