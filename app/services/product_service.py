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
    products=db.query(Product).all()
    return products

def get_product_by_id(id:int,db:Session):
    product=db.query(Product).filter(Product.id==id).first()
    if product:
        return product

def update_product_by_id(id:int,update_product:ProductUpdate,db:Session):
    product=db.query(Product).filter(Product.id==id).first()
    if product:
        product.name=update_product.name
        product.description=update_product.description
        product.price=update_product.price
        product.stock=update_product.stock
        return product
    raise HTTPException(status_code=404,detail='Product not exist')

def delete_product_by_id(id:int):
    product=db.query(Product).filter(product.id==id).first()
    if product:
        db.delete(product)
        db.commit()
        db.refresh(product)
        return product

    raise HTTPException(status_code=404,detail='Product not exist')