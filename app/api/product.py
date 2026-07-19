from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from services.product_service import product_create,all_products,get_product_by_id,update_product_by_id,delete_product_by_id,pagination,search
from db.database import get_db
from schemas.product import ProductCreate,ProductResponse,ProductUpdate,GetAllProductsResponse
from dependencies.dependencies import get_current_user


router=APIRouter()

@router.post('/createproduct',response_model=ProductResponse)
def create_product(product:ProductCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
      return product_create(product,db)

@router.get('/get_all_product',response_model=list[ProductResponse])
def get_all_product(db:Session=Depends(get_db)):
      return all_products(db)

@router.get('/get_product_by_id{id}',response_model=ProductResponse)
def get_by_id(id:int,db:Session=Depends(get_db)):
      return get_product_by_id(id,db)

@router.put('/update_product_by_id{id}',response_model=ProductResponse)
def update_by_id(id:int,update_product:ProductUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
      return update_product_by_id(id,update_product,db)

@router.delete('/delete_product_by_id{id}',response_model=ProductResponse)
def delete_product(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
      return delete_product_by_id(id,db)

@router.get('/pagination',response_model=GetAllProductsResponse)
def page_ination(lmt:int=10,page:int=1,db:Session=Depends(get_db)):
      return pagination(lmt,page,db)

@router.get('/search',response_model=GetAllProductsResponse)
def search_by_keyword(keyword:str,db:Session=Depends(get_db)):
      return search(keyword,db)