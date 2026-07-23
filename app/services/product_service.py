from fastapi import HTTPException,Depends
from sqlalchemy import func, asc, desc
from sqlalchemy.orm import Session
from math import ceil

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

        db.commit()
        db.refresh(product)
        
        return product
    raise HTTPException(status_code=404,detail='Product not exist')

def delete_product_by_id(id:int,db:Session):
    product=db.query(Product).filter(Product.id==id).first()
    if product:
        db.delete(product)
        db.commit()
        return product

    raise HTTPException(status_code=404,detail='Product not exist')

"""
def pagination(lmt:int,page:int,db:Session):
    off_set=(page-1)*lmt
    products=db.query(Product).limit(lmt).offset(off_set).all()
    return {
        'products':products
        }

def search(keyword:str,db:Session):
    keyword=keyword.lower()
    keyword_products=db.query(Product).filter(func.lower(Product.name).like(f"%{keyword}%"))
    return {
        'products':keyword_products
    }
"""

def advanced_search(db:Session, search:str|None = None, min_price:float|None = None, max_price:float|None = None, sort: str|None = None, order: str = 'asc', page:int = 1, lmt: int = 10):
    query=db.query(Product)

    #search
    if search:
        search=search.lower()
        query=query.filter(or_(func.lower(Product.name).like(f"%{search}%"),func.lower(Product.description).like(f"%{search}%")))
    
    # price filter
    if min_price is not None:
        query=query.filter(Product.price>=min_price)
    
    if max_price is not None:
        query=query.filter(Product.price<=max_price)

    # sorting
    if sort:
        sort_fields={
            "name":Product.name,
            "price":Product.price,
            "stock":Product.stock
        }

        column=sort_fields.get(sort)

        if not column:
            raise HTTPException(status_code=400,detail="Invalid sort field")

        if order.lower()=='desc':
            query=query.order_by(desc(column))
        else:
            query=query.order_by(asc(column))
    
    total=query.count()
        
    #pagination
    off_set=(page-1)*lmt

    products=query.offset(off_set).limit(lmt).all()

    return{
        "page": page,
        "limit": lmt,
        "total": total,
        "total_pages": ceil(total / lmt),
        "products": products
        }