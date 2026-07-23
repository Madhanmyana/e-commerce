from sqlalchemy.orm import Session
from fastapi import HTTPException

import schemas
import models

def create_category(category:schemas.product.CategoryCreate,db:Session):
    if db.query(models.product.Category).filter(models.product.Category.name==category.name).first():
        raise HTTPException(status_code=400,detail='category alredy exist')
    
    new_category=models.product.Category(
        name=category.name,
        description=category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db:Session):
    all_categories=db.query(models.product.Category).all()
    return {
        'categoryies':all_categories
    }

def get_category_by_id(id:int,db:Session):
    category=db.query(models.product.Category).filter(models.product.Category.id==category.id).first()
    if category:
        return category
    
    raise HTTPException(status_code=404,detail='category not exist')
    
def update_category_by_id(id:int,update_category:schemas.product.CategoryUpdate,db:Session):
    category=db.query(models.product.Category).filter(models.product.Category.id==id).first()
    if category:
        category.name=update_category.name
        category.description=update_category.description

        db.commit()
        db.refresh(category)

        return category
    
    raise HTTPException(status_code=404,detail='category not exist')

def delete_category(id:int,db:Session):
    category=db.query(models.product.Category).filter(models.product.Category.id==id).first()
    if category:
        db.delete(category)
        db.commit()
        return category

    raise HTTPException(status_code=404,detail='category not exist')
