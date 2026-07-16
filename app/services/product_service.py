from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate, ProductResponse, ProductUpdate
from dependencies.dependencies import get_current_user

def product_create(product:ProductCreate,db:Session):
    if db.query(Product).filter(Product.name==product.name).first():
        raise HTTPException(status_code=400,detail='product alredy exist')
    
    new_product=Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def all_products(db:Session):
    products=db.query(Products).all()
    return products