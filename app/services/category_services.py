from sqlalchemy.orm import Session
from fastapi import HTTPException

from schemas.product import CategoryCreate,CategoryUpdate
from models.product import Category
def create_category(category:CategoryCreate,db:Session):
    if db.query(Category).filter(Category.name==category.name).first():
        raise HTTPException(status_code=400,detail='category alredy exist')
    
    new_category=Category(
        name=category.name,
        description=category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db:Session):
    all_categories=db.query(Category).all()
    return {
        'categories':all_categories
    }

def get_category_by_id(id:int,db:Session):
    category=db.query(Category).filter(Category.id==id).first()
    if category:
        return category
    
    raise HTTPException(status_code=404,detail='category not exist')
    
def update_category_by_id(id:int,update_category:CategoryUpdate,db:Session):
    category=db.query(Category).filter(Category.id==id).first()
    if category:
        category.name=update_category.name
        category.description=update_category.description

        db.commit()
        db.refresh(category)

        return category
    
    raise HTTPException(status_code=404,detail='category not exist')

def delete_category(id:int,db:Session):
    category=db.query(Category).filter(Category.id==id).first()
    if category:
        db.delete(category)
        db.commit()
        return category

    raise HTTPException(status_code=404,detail='category not exist')