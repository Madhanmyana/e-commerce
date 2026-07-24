from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from services.category_services import create_category,get_all_categories,get_category_by_id,update_category_by_id,delete_category
from schemas.product  import CategoryCreate,CategoryResponse,GetAllCategoriesResponse
from db.database import get_db
from dependencies.dependencies import get_current_user,require_admin

router=APIRouter()

@router.post('/categories',response_model=CategoryResponse)
def createcategory(category:CategoryCreate,
                    db:Session=Depends(get_db),
                    current_user=Depends(require_admin)):
                    
                    return create_category(category,db)

@router.get('/categories',response_model=GetAllCategoriesResponse)
def all_categories(db:Session=Depends(get_db)):
    return get_all_categories(db)

@router.get('/categories{id}',response_model=CategoryResponse)
def category_by_id(id:int,db:Session=Depends(get_db)):
    return get_category_by_id(id,db)

@router.put('/categories{id}',response_model=CategoryResponse)
def update_category(id:int,
                    db:Session=Depends(get_db),
                    current_user=Depends(require_admin)):
                    
                    return update_category_by_id

@router.delete('/categories{id}',response_model=CategoryResponse)
def delete_category_id(id:int,
                        db:Session=Depends(get_db),
                        current_user=Depends(require_admin)):

                        return delete_category(id,db)