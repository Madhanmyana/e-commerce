from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from services.product_service import product_create
from db.database import get_db
from schemas.product import ProductCreate,ProductResponse,ProductUpdate
from dependencies.dependencies import get_current_user


router=APIRouter()

@router.post('/createproduct',response_model=ProductResponse)
def create_product(product:ProductCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
      return product_create(product,db)
